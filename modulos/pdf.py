# -*- encoding: utf-8 -*-

from reportlab.pdfgen import canvas #Biblioteca para gerar pdf
from reportlab.lib.utils import ImageReader #Biblioteca para inserir Imagem no pdf
import math

class pdf:

    def __init__(self):
        self.file = None
        self.idCard = 0
        self.pg = 0
        self.conf = {
            "size":(841.8897637795277, 595.2755905511812),
            "larguraCarta" : 0,
            "alturaCarta" : 0,
            "perLine": 0,
            "perCollum": 0
        }
        self.setConf()

    def setConf(self):
        '''Define as configurações de impressão'''
    
        larguraPagina =841.8897637795277
        alturaPagina = 595.2755905511812
        larguraCarta = 181.41720855608912+2 #6.4/0.0352778
        alturaCarta = 249.44866176462256+4  #8.8/0.0352778
        #larguraCarta = 100#181.41720855608912 #6.4/0.0352778
        #alturaCarta = 160#249.44866176462256  #8.8/0.0352778
        size = (larguraPagina, alturaPagina)
        perLine = math.floor(larguraPagina/larguraCarta)
        perCollum = math.floor(alturaPagina/alturaCarta)
        margH = (larguraPagina - (larguraCarta*perLine) ) / (perLine+1)
        margV = (alturaPagina - (alturaCarta*perCollum) ) / (perCollum+1)

        self.conf = {
            "size":size,
            "larguraCarta":larguraCarta,
            "alturaCarta":alturaCarta,
            "perLine":perLine,
            "perCollum":perCollum,
            "margH":margH,
            "margV":margV
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
        offSetH = coluna * (self.conf['margH']+self.conf['larguraCarta'])
        offSetW = linha * (self.conf['margV']+self.conf['alturaCarta'])

        x1 = offSetH + self.conf['margH']
        x2 = x1 + self.conf['larguraCarta']
        y1 = offSetW + self.conf['margV']
        y2 = y1 + self.conf['alturaCarta']

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


    def printCard(self,pathImage):
        '''Desenha a imagem na folha'''

        cut = True

        point = self.positionDraw()
            
        #Imagem
        image = ImageReader(pathImage)

        #Desenha a imagem
        self.file.drawImage(image, point['x1'], point['y1'], width=self.conf['larguraCarta'], height=self.conf['alturaCarta'])
        self.file.setStrokeColorRGB(0,0,0) 

        #Traça a silhueta
        self.file.line( point['x1'],point['y1'],point['x2'],point['y1'])#Base
        self.file.line( point['x2'],point['y1'],point['x2'],point['y2'])#Borda Direita
        self.file.line( point['x2'],point['y2'],point['x1'],point['y2'])#Top
        self.file.line( point['x1'],point['y2'],point['x1'],point['y1'])#Borda Esquerda

        if cut:
            self.printCut()
        self.countCard()