from os import name
from urllib.parse import urldefrag
from urllib.parse import urlparse
from unidecode import Cache
from modulos.extraction import manager
from modulos import pdf, persistence, request, menu
from modulos.view import View
from modulos.cmd import CMD
from ast import literal_eval
import json
import random

class Main:
    def __init__(self):
        # Import de modulos
        self.menu = menu.Menu()
        self.persistence = persistence.persistence()
        self.request = request.request()
        self.extractionManager = manager.Manager()
        self.pdf = pdf.pdf()
        self.args = CMD()


    def input(self):
        return self.menu.selection(View.listOptions())
    
    def optNew(self,url=""):
        #Cria um deck passo a passo
        if url=="":
            url = input("Digite a url: ")
        self.metaData(url)
        self.requestUrl(url)
        self.makeDeck()
        self.getImg()
        self.myDeck()
    
    def optOld(self,keyDeck=""):
        #Verifica qual o deck a ser trabalhado
        if keyDeck=="":
            keyDeck = self.menu.selection( View.listDecks() )
        self.persistence.meta(keyDeck)        
        #Continua o processo de onde parou e renderiza um novo PDF
        self.metaData()
        self.requestUrl(self.meta['url'])
        self.makeDeck()               
        self.getImg()
        self.myDeck()

    def requestUrl(self, url):
        """ Request da Pagina """
        if(not self.persistence.processOk("html")):
            #Faz Download da pagina 
            self.html = self.request.downloadHTML(url)
            #Persiste a pagina 
            self.persistence.persistFile(self.html, "html")
        else:
            #Le o html do arquivo
            self.html = self.persistence.load("html")

    def makeDeck(self):
        """ Cataloga o Deck """
        if(not self.persistence.processOk("deck")):
            #Preparando para trabalhar com o deck
            self.scraper.load(self.html, self.persistence.nameDeck, self.persistence.pastaDeck)
            self.deck = self.scraper.catalogarDeck()
            #Formata o Deck
            prettyDeck = str( json.dumps(self.deck, indent=4, sort_keys=False) )
            #Persiste o Deck 
            self.persistence.persistFile( prettyDeck, "deck")
        else:
            #Le o arquivo de catalogo do Deck
            self.deck = literal_eval(self.persistence.load("deck"))

    def getImg(self):
        """ Faz Download das Imagens """
        if(not self.persistence.processOk("img")):
            listUrl = ''
            #Preparando para trabalhar com o deck
            print("Cards:")
            for type in self.deck:
                for card in self.deck[type]:
                    print(str(card["qtd"])+"\tx\t"+card['name'])
                    listUrl = listUrl + card['url']+'\n'
                    #Faz Download da imagem
                    url = "https://"+card['url']
                    name = "Deck/img/"+card['img']+'.jpg'
                    #Verifica se a imagem ja existe
                    if(not self.persistence.it_is_ok(name)):
                        self.request.downloadIMG(url, name)
            self.persistence.persistFile(listUrl, "img")

    def myDeck(self):
        #Cria o canvas do PDF
        self.pdf.makePdf(self.persistence.pastaDeck+"/"+self.persistence.nameDeck+".pdf")
        #Preenche o canvas com as imagens do Deck
        for type in self.deck:
            for card in self.deck[type]:
                if(card['qtd'] <= 4):#So desenha caso tenha 4 ou menos quantidades de uma carta
                    for i in range(card['qtd']):
                        self.pdf.printCard("Deck/img/"+card['img']+'.jpg')
        self.pdf.close()
    
    def myDeckRandom(self):
        #Cria lista
        l=[]
        for type in self.deck:
            for card in self.deck[type]:
                for i in range(card['qtd']):
                    l.append(card)
        random.shuffle(l)
    
        #Cria o canvas do PDF
        self.pdf.makePdf(self.persistence.pastaDeck+"/"+self.persistence.nameDeck+"_Random.pdf")
        for card in l:
            self.pdf.printCard("Deck/img/"+card['img']+'.jpg')
        self.pdf.close()

    def dirDeck(self):
        """ Verifica se existe um diretorio proprio para o deck """
        if not self.persistence.it_is_ok(self.persistence.pastaDeck):
            #Cria o diretorio que ficara todos os arquivos do deck
            if(not self.persistence.persistDir(self.persistence.pastaDeck)):
                print("Erro ao criar Diretorio")
        else:
            print("Ja existe um diretorio com este nome")

    def metaData(self, url=""):
        """ Cria um arquivos somente com meta dados """
        if(not self.persistence.processOk("meta")):
            #Extrai metadados da url
            keyDeck = url.split("/")[-1].split("=")[-1]
            site = urlparse(url).netloc
            #Cria um Objeto para ser salvo
            self.meta = { "nameDeck":keyDeck, "dirDeck":"Deck/deck_"+keyDeck, "extractor":site, "url":url }
            prettyMeta = str( json.dumps(self.meta, indent=4, sort_keys=True) )
            #Persiste os meta dados
            self.persistence.meta(keyDeck)
            self.dirDeck()
            self.persistence.persistFile( prettyMeta, "meta")
        else:
            #Le o arquivo de meta dados do Deck
            self.meta = literal_eval(self.persistence.load("meta"))
        #selecionar o extractor / scraper
        self.scraper = self.extractionManager.selectExtractor(self.meta["extractor"])

    def run(self):
        flag = self.args.flags()
        #Fluxo
        if not (bool(flag.url) or bool(flag.id)):
            arg = self.menu.selection(View.listOptions())
            if(arg == "New"):
                self.optNew()
            elif(arg == "Old"):
                self.optOld()
        elif bool(flag.url):
            self.optNew(flag.url)
        elif bool(flag.id):
            self.optOld(flag.id)


Main().run()