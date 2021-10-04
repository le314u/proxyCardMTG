from modulos.extraction import manager
from modulos import pdf, persistence, request, menu
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
        arg = self.menu.selection({
            "Exemplo":"Cria um arquivo de modelo",
            "New":"Cria um novo deck",
            "Old":"Cria um deck ja existente"
        })

        if(arg == "New"):
            url = input("Digite a url: ")
            self.setUrl(url)
            self.dirDeck()
            self.requestUrl(url)
            self.makeDeck()
            self.getImg()
            self.myDeck()

        elif(arg == "Old"):
            lista = self.persistence.listDeck()
            arg = self.menu.selection( lista )
            self.persistence.nameDeck = arg
            self.persistence.pastaDeck = "Deck/deck_"+arg
            self.deck = literal_eval(self.persistence.load("deck"))
            self.getImg()
            self.myDeck()
            self.myDeckRandom()

        elif(arg == "Exemplo"):
            nameSpace = input("Digite o nome do deck: ")
            self.persistence.setData(nameSpace)
            self.dirDeck()
            self.persistence.persistFile('snapShot da pagina html', "html")
            deck = { "Tipo": [ { "qtd": 1, "name": "Nome", "url": "https://link/img.png", "img": "nomeDaImagem" },{ "qtd": 1, "name": "Nome", "url": "https://link/img.png", "img": "nomeDaImagem" } ] }
            prettyDeck = str( json.dumps(deck, indent=4, sort_keys=False) )
            self.persistence.persistFile( prettyDeck, "deck")
            self.persistence.persistFile('https://link/img.png', "img")


    def setUrl(self, url):
        """ Seta a URL """
        #Pega dados essenciais da URL
        self.persistence.processeUrl(url)
        #selecionar o extractor / scraper
        self.scraper = self.extractionManager.selectExtractor(self.persistence.site)

    def dirDeck(self):
        """ Verifica se existe um diretorio proprio para o deck """
        if not self.persistence.it_is_ok(self.persistence.pastaDeck):
            #Cria o diretorio que ficara todos os arquivos do deck
            if(not self.persistence.persistDir(self.persistence.pastaDeck)):
                print("Erro ao criar Diretorio")
        else:
            print("Ja existe um diretorio com este nome")

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
            #Cataloga o Deck
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
                for i in range(int(card['qtd'])):
                    l.append(card)
        random.shuffle(l)
    
        #Cria o canvas do PDF
        self.pdf.makePdf(self.persistence.pastaDeck+"/myDeckRandom.pdf")
        for card in l:
            self.pdf.printCard("Deck/img/"+card['img']+'.jpg')
        self.pdf.close()



Main()