from os import name
from rich import print
from modulos.deck import Deck
from modulos.html import Html
from modulos.meta import Meta
from modulos.extraction import extraction
from modulos.view.view import View
from modulos.pdf import Pdf
from modulos.cli.cmd import CMD
from modulos.persistence import Persistence
from modulos.request import Request


class State:
    def __init__(self):
        self.states = ["META","HTML","DECK","DOWNLOAD","PDF","FINISH"]
        self.state = -1
        self.error = -1
    
    def next(self):
        self.state = (self.state+1) % len(self.states)        

    def setError(self):
        self.error = 1

    def reset(self):
        self.error = -1
        self.state = -1

    def hasError(self):
        return self.error == 1

    def setState(self,state):
        if state in self.states:
            self.states.index(state)
    
    def getState(self):
        if(self.state!= -1):
            return str( self.states[self.state] )
        else:
            return "OFF"




class Main:
    def __init__(self):
        # Import de modulos
        #Steps
        self.html = Html()
        self.deck = Deck()
        self.meta = Meta()
        self.persistence = Persistence()
        self.request = Request()
        self.pdf = Pdf()
        self.args = CMD()
        self.conf = {
            "html":"",
            "scraper":"",
            "deck":"",
            "meta":""
        }
        self.state = State()

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
  
    def flow(self,url=""):
        self.state.setState("META")

        self.state.next()
        self.stepMETA(url)

        self.state.next()
        self.stepHTML(self.conf["meta"]["url"])

        self.state.next()
        self.stepDECK()

        self.state.next()
        self.getImg()

        self.state.next()
        self.stepPDF()
        
        self.state.setState("FINISH")



    def run(self):
        FLAGS = self.args.flags()

        #Se não tiver Flag inicia a TUI
        if not (bool(FLAGS.url) or bool(FLAGS.id)):
            app = View()
            app.setConf(self.flow,self.persistence.setupDeck,self.state)
            app.run()
        #CLI -url 
        elif bool(FLAGS.url):
            self.flow(FLAGS.url)  
        #CLI -id
        elif bool(FLAGS.id):
            #Verifica qual o deck a ser trabalhado
            self.persistence.setupDeck( FLAGS.id )       
            #Continua o processo de onde parou e renderiza um novo PDF
            self.flow()


Main().run()