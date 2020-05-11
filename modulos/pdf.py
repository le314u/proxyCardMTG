# -*- encoding: utf-8 -*-

from reportlab.pdfgen import canvas #Biblioteca para gerar pdf
from reportlab.lib.utils import ImageReader #Biblioteca para inserir Imagem no pdf

class pdf:
    def __init__(self):
        self.file = None
        self.size=(841.8897637795277, 595.2755905511812)
        self.idCard = 0
        self.pg = 0
        
    def makePdf(self, path):
        self.file = canvas.Canvas(path,pagesize=self.size)

    def close(self):
        '''Fecha o Arquivo PDF'''
        self.file.save()

    def countCard(self):
        '''Contador circular para posicionar a imagem na folha'''
        self.idCard = (self.idCard+1) 
        if self.idCard == 8 : #Cria uma outra pagina
            self.file.showPage()
            self.pg = self.pg + 1
            self.idCard = 0
            
    def printCard(self,pathImage):
        '''Printa a imagem na folha'''
        #Variavel
        cut = True

        #Tamanho da carta
        larguraCarta = 181.41720855608912+2 #6.4/0.0352778
        alturaCarta = 249.44866176462256+4  #8.8/0.0352778

        #Tamanho da pagina
        larguraPagina = self.size[0]
        alturaPagina = self.size[1]
        #Margem
        margE = (larguraPagina - (larguraCarta*4) ) / 5
        margB = (alturaPagina - (alturaCarta*2) ) / 3

        #Deslocamento
        if ( (self.idCard%4) == 0):
            offSetL = (margE +larguraCarta) * (self.idCard%4)
        else:
            #Espaço entre Cartas
            spaceInterL = margE #identico a margem Esquerda
            offSetL = (spaceInterL +larguraCarta) * (self.idCard%4)

        if (((self.idCard%8)-4) >= 0):
            #Espaço entre Cartas
            spaceInterW = margB #identico a margem Base
            offSetW = spaceInterW + alturaCarta
        else:
            offSetW = 0

        #Quinas da carta
        x1 = margE + offSetL
        x2 = x1 + larguraCarta
        y1 = margB + offSetW
        y2 = y1 + alturaCarta
        
        #Imagem
        image = ImageReader(pathImage)

        #Desenha a imagem
        self.file.drawImage(image,x1,y1, width=larguraCarta,height=alturaCarta)

        self.file.setStrokeColorRGB(0,0,0) 
        #Traça a silhueta
        self.file.line( x1,y1,x2,y1)#Base
        self.file.line( x2,y1,x2,y2)#Borda Direita
        self.file.line( x2,y2,x1,y2)#Top
        self.file.line( x1,y2,x1,y1)#Borda Esquerda

        if cut == True :
            #Altera a cor do traço que informa onde deve ser o corte 
            self.file.setStrokeColorRGB(255,0,0)
            #Borda a ser cortada
            self.file.line( x1,y1+4,x1+4,y1)#Quina EI
            self.file.line( x2-4,y1,x2,y1+4)#Quina DI
            self.file.line( x2-4,y2,x2,y2-4)#Quina DS
            self.file.line( x1+4,y2,x1,y2-4)#Quina ES
            #retorna a cor preta como padrão de traço
            self.file.setStrokeColorRGB(0,0,0)  

        #Incrementa o 'id' de posicionamento
        self.countCard()