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

        #Tamanho da carta
        larguraCarta = 181.41720855608912 #6.4/0.0352778
        alturaCarta = 249.44866176462256  #8.8/0.0352778

        #Margem
        margE = 23.244185911034243        #(larguraPagina - (larguraCarta*4) ) / 5
        margB = 32.12608900731201   #(alturaPagina - (alturaCarta*2) ) / 3

        #Deslocamento
        if ( (self.idCard%4) == 0):
            offSetL = (margE +larguraCarta) * (self.idCard%4)
        else:
            #Espaço entre Cartas
            spaceInterL = 23.244185911 #identico a margem Esquerda
            offSetL = (spaceInterL +larguraCarta) * (self.idCard%4)

        if (((self.idCard%8)-4) >= 0):
            #Espaço entre Cartas
            spaceInterW = 32.12608900731201 #identico a margem Base
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

        #Caso queira colocar a silhueta de outra cor
        #self.file.setStrokeColorRGB(255,0,0)    

        #Traça a silhueta
        self.file.line( x1,y1,x2,y1)#Base
        self.file.line( x2,y1,x2,y2)#Borda Direita
        self.file.line( x2,y2,x1,y2)#Top
        self.file.line( x1,y2,x1,y1)#Borda Esquerda
        
        #Incrementa o 'id' de posicionamento
        self.countCard()
        

    

    