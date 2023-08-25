from os import name
from modulos.deck import Deck
from modulos.html import Html
from modulos.meta import Meta
from modulos.extraction import extraction
from modulos import pdf, persistence, request, menu
from modulos.view import View
from modulos.cmd import CMD

class Main:
    def __init__(self):
        # Import de modulos
        #Steps
        self.html = Html()
        self.deck = Deck()
        self.meta = Meta()
        self.menu = menu.Menu()
        self.persistence = persistence.persistence()
        self.request = request.request()
        self.pdf = pdf.pdf()
        self.args = CMD()
        self.conf = {
            "html":"",
            "scraper":"",
            "deck":"",
            "meta":""
        }

    def stepHTML(self, url=""):
        """ Request da Pagina """ 
        att = {};
        if(not self.persistence.processOk("html")):
            att["html"] = self.html.loadUrl(self.request,url)
            self.html.dumpHTML(self.persistence,att["html"])
        else:
            #Le o html do arquivo
            att["html"] = self.html.loadFile(self.persistence)
        self.conf.update(att)

    def stepDECK(self):
        """ Cataloga o Deck """
        att = {};
        if(not self.persistence.processOk("deck")):
            att["deck"] = self.deck.create(self.conf["scraper"], self.conf["html"])
            self.deck.dumpDECK(self.persistence,att["deck"])
        else:
            #Le o arquivo de catalogo do Deck
            att["deck"]=self.deck.loadFile(self.persistence)
        self.conf.update(att)

    def stepPDF(self):
        #Cria o canvas do PDF
        self.pdf.dumpPDF(self.persistence,self.conf["deck"])

    def stepMETA(self,url=""):
        """ Cria um arquivos somente com meta dados """
        att={}
        if(url != "" or not self.persistence.processOk("meta")):
            att = self.meta.meta(url)
            self.persistence.setupDeck(att["meta"]["nameDeck"])
            self.meta.dumpMETA(self.persistence, att["meta"])
        else:
            att = self.meta.loadFile(self.persistence)
        self.conf.update(att)

    def stepPDF(self):
        self.pdf.dumpPDF(self.persistence,self.conf["deck"])

    def getImg(self):
        """ Faz Download das Imagens """
        if(not self.persistence.processOk("img")):
            self.deck.dumpIMG(self.request, self.persistence, self.conf["deck"])
   
    

    def input(self):
        return self.menu.selection(View.listOptions())
        
    def optNew(self,url=""):
        #Cria um deck passo a passo
        if url=="":
            url = input("Digite a url: ")
        self.flow(url)  
    

    def optOld(self,keyDeck=""):
        #Verifica qual o deck a ser trabalhado
        if keyDeck=="":
            keyDeck = self.menu.selection( View.listDecks() )
        self.persistence.setupDeck(keyDeck)       
        #Continua o processo de onde parou e renderiza um novo PDF
        self.flow()

    def flow(self,url=""):
        self.stepMETA(url)
        self.stepHTML(self.conf["meta"]["url"])
        self.stepDECK()
        self.getImg()
        self.stepPDF()

    def run(self):
        FLAGS = self.args.flags()
        #Fluxo
        if not (bool(FLAGS.url) or bool(FLAGS.id)):
            arg = self.menu.selection(View.listOptions())
            if(arg == "New"):
                self.optNew()
            elif(arg == "Old"):
                self.optOld()
        elif bool(FLAGS.url):
            self.optNew(FLAGS.url)
        elif bool(FLAGS.id):
            self.optOld(FLAGS.id)

Main().run()

#Download da página HTML
#Extração das cartas presentes no deck
#Download das imagens das cartas
#Criação do arquivo PDF