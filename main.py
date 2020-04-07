# -*- encoding: utf-8 -*-
import requests #Biblioteca que faz requisições http
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
from reportlab.pdfgen import canvas #Biblioteca para gerar pdf
from reportlab.lib.utils import ImageReader #Biblioteca para inserir Imagem no pdf

# Variaveis
url = input("Digite a url: ")
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
verbose = True
Deck = {}

#Cria a pasta onde ira persistir as imagens do deck
nameDeck = url.split("/")[-1].split("&")[-1]
pastaDeck = "deck_"+nameDeck
try:
    os.mkdir("./"+pastaDeck)
except:
    print("Este deck ja foi Processado, caso esteja corrompido delete a pasta "+pastaDeck)
    exit()

#Faz download da pagina
if(verbose):
    print("Acessando pagina: "+url)
httpRequest = requests.get(url, headers=headers)
httpEstruct = BeautifulSoup(httpRequest.text, 'lxml')

#Cataloga o Deck (pegando [qtd, nome, img, css])
linhas = httpEstruct.tbody.findAll('tr')
nKey = "";
for linha in linhas:#Passa por todas as linhas (cada linha é uma carta)
    colunas = linha.findAll('td',recursive=False)
    if len(colunas) == 1:
        if len(colunas[0].contents) == 1:
            #Chegou ao fim onde informa o total de cartas
            if(verbose):
                print("Deck Completo"+colunas[0].contents[0]+" "*60)
                break
        else:
            #label que define o tipo da carta (criatura, artefato,magica)
            nKey = colunas[0].contents[0].replace(" ","",-1)
            Deck[nKey] = []
            if(verbose):
                print("Catalogando :"+nKey+" "*60)

    else:
        qtd = colunas[0].string
        name = colunas[1].string
        if(verbose):
                print("Fazendo download de: "+name,end="\t\t\t\t\r\r")
        css = linha.find("a")["data-tooltip"]
        img = httpEstruct.find_all(id="mystickytooltip")[0].find(id="lazy_"+css)['lazy-src'][2:]
        binImg = requests.get("https://"+img, headers=headers)
        open('./'+pastaDeck+"/"+css+".jpg",'wb').write(binImg.content)
        #Quantidade e nome da carta
        Deck[nKey].append({"qtd":int(qtd),"name":name,"img":img,"css":css,})

def printCard(id,pathImage,pg):
    # OBS cabe 6 em uma pagina

    #Tamanho da carta
    lCard = 6.4/0.0352778
    wCard = 8.8/0.0352778

    #Margem
    margE = 23.244185911        #(larguraPagina - (larguraCarta*4) ) / 5
    margB = 32.12608900731201   #(alturaPagina - (alturaCarta*4) ) / 3

    #Deslocamento
    if ( (id%4) == 0):
        offSetL = (margE +lCard) * (id%4)
    else:
        #Espaço entre Cartas
        spaceInterL = 23.244185911 #identico a margem Esquerda
        offSetL = (spaceInterL +lCard) * (id%4)

    if (((id%8)-4) >= 0):
        #Espaço entre Cartas
        spaceInterW = 32.12608900731201 #identico a margem Base
        offSetW = spaceInterW + wCard
    else:
        offSetW = 0

    #Quinas da carta
    x1 = margE + offSetL
    x2 = x1 + lCard
    y1 = margB + offSetW
    y2 = y1 + wCard

    #Traça a silhueta
    pg.line( x1,y1,x2,y1)#Base
    pg.line( x2,y1,x2,y2)#Borda Direita
    pg.line( x2,y2,x1,y2)#Top
    pg.line( x1,y2,x1,y1)#Borda Esquerda

    #Imagem
    image = ImageReader(pathImage)

    #Desenha a imagem
    pg.drawImage(image,x1,y1, width=lCard,height=wCard)


#Cria o Arquivo Pdf (595.2755905511812, 841.8897637795277)
A4_in=(841.8897637795277, 595.2755905511812)
arq = canvas.Canvas("./"+pastaDeck+"/Deck.pdf",pagesize=A4_in)

id=0
for tipo in Deck: #Itera todos os tipos de cartas
    for card in Deck[tipo]: #Itera todas as cartas
        for index in range(0,card['qtd']): #Itera a mesma carta 'qtd' de vez
            #Printa a Card
            printCard(id,'./'+pastaDeck+"/"+card['css']+".jpg",arq)
            id = (id+1) 
            if id == 8 : #Cria uma outra pagina
                arq.showPage()
                id = 0


arq.showPage()
arq.save()