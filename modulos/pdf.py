# -*- encoding: utf-8 -*-

from reportlab.pdfgen import canvas #Biblioteca para gerar pdf
from reportlab.lib.utils import ImageReader #Biblioteca para inserir Imagem no pdf
import math

class pdf:

    def __init__(self):
        self.file = None
        self.idCard = 0
        self.pg = 0
        self.conf = {}
        self.setConf()


    def setConf(self):
        '''Define as configurações de impressão'''
        CM2PT = 28.3464567
        wPage= lambda cm: cm * CM2PT
        hPage = lambda cm: cm * CM2PT
        wCard = lambda cm: cm * CM2PT + 2
        hCard = lambda cm: cm * CM2PT + 4
        perLine = lambda wPage, wCard : math.floor(wPage/wCard)
        perCollum = lambda hPage, hCard : math.floor(hPage/hCard)
        horizMargin = lambda wPage, wCard, perLine : (wPage - (wCard*perLine) ) / (perLine+1)
        vertMargin = lambda  hPage, hCard, perCollum: (hPage - (hCard*perCollum) ) / (perCollum+1)

        self.conf = {
            "size": (wPage(21), hPage(29.7)),
            "wCard": wCard(6.4),
            "hCard": hCard(8.8),
            "perLine": perLine(wPage(21), wCard(6.4)),
            "perCollum": perCollum(hPage(29.7), hCard(8.8)),
            "horizMargin": horizMargin(wPage(21), wCard(6.4), perLine(wPage(21), wCard(6.4))),
            "vertMargin": vertMargin(hPage(29.7), hCard(8.8), perCollum(hPage(29.7), hCard(8.8)))
    }

    def text(self, text):
        ''' Escreve um texto na pagina'''
        self.file.drawString(420,585,text)

    def newPage(self):
        '''Cria uma nova Pagina'''
        self.file.showPage()
        self.pg = self.pg + 1
        self.idCard = 0

    def makePdf(self, path):
        '''Inicia o Arquivo pdf'''
        self.pg = 0
        self.idCard = 0
        self.file = canvas.Canvas(path,pagesize=self.conf['size'])

    def close(self):
        '''Fecha o Arquivo PDF'''
        self.file.save()

    def countCard(self):
        '''Contador circular para posicionar a imagem na folha'''
        self.idCard = (self.idCard+1) 
        if self.idCard == (self.conf['perLine']*self.conf['perCollum']) : #Cria uma outra pagina
            self.file.showPage()
            self.pg = self.pg + 1
            self.idCard = 0

    def positionDraw(self):
        '''Define em quais pontos ocorrerá o desenho da carta'''

        #Define qual coluna será desenhado
        coluna = self.idCard%self.conf['perLine']
        linha = (math.floor(self.idCard/self.conf['perLine']))

        #Deslocamento Horizontal de acordo com qual coluna será desenhada
        offSetH = coluna * (self.conf['horizMargin'] + self.conf['wCard'])
        offSetW = linha * (self.conf['vertMargin'] + self.conf['hCard'])

        x1 = offSetH + self.conf['horizMargin']
        x2 = x1 + self.conf['wCard']
        y1 = offSetW + self.conf['vertMargin']
        y2 = y1 + self.conf['hCard']

        return {
            "x1":x1,
            "x2":x2,
            "y1":y1,
            "y2":y2
        }

    def printCut(self):
        '''Desenha os cortes na quina da carta'''
        point = self.positionDraw()
        #Altera a cor do traço que informa onde deve ser o corte 
        self.file.setStrokeColorRGB(255,0,0)
        #Borda a ser cortada
        self.file.line( point['x1'],point['y1']+4,point['x1']+4,point['y1'])#Quina EI
        self.file.line( point['x2']-4,point['y1'],point['x2'],point['y1']+4)#Quina DI
        self.file.line( point['x2']-4,point['y2'],point['x2'],point['y2']-4)#Quina DS
        self.file.line( point['x1']+4,point['y2'],point['x1'],point['y2']-4)#Quina ES
        #retorna a cor preta como padrão de traço
        self.file.setStrokeColorRGB(0,0,0)  


    def printCard(self,pathImage,cut=True):
        '''Desenha a imagem na folha'''
        point = self.positionDraw()
            
        #Imagem
        image = ImageReader(pathImage)

        #Desenha a imagem
        self.file.drawImage(image, point['x1'], point['y1'], width=self.conf['wCard'], height=self.conf['hCard'])
        self.file.setStrokeColorRGB(0,0,0) 

        #Traça a silhueta
        self.file.line( point['x1'],point['y1'],point['x2'],point['y1'])#Base
        self.file.line( point['x2'],point['y1'],point['x2'],point['y2'])#Borda Direita
        self.file.line( point['x2'],point['y2'],point['x1'],point['y2'])#Top
        self.file.line( point['x1'],point['y2'],point['x1'],point['y1'])#Borda Esquerda

        if cut:
            self.printCut()

        self.countCard()