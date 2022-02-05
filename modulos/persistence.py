from pathlib import Path
import os
from urllib.parse import urlparse


class persistence:

    def __init__(self):
        self.nameDeck = ''
        self.pastaDeck = ''
        try:#Cria as pastas essenciais para que o programa funcione
            self.persistDir("Deck")
            self.persistDir("Deck/img")
        except:
            pass
        
    def meta(self, nameDeck):
        '''Carrega os metaDados de um deck'''
        self.nameDeck = nameDeck
        self.pastaDeck = "Deck/deck_"+nameDeck
    
    def processOk(self, extensao):
        ''' Verifica o que ja foi feito '''
        #Arquivo esta ok?
        return self.it_is_ok(self.pastaDeck+"/"+self.nameDeck+"."+extensao)

    def it_is_ok(self, path):
        ''' Verifica se existe um arquivo de acordo com o path '''
        file = Path(path)
        return (file.is_file() or file.is_dir())

    def persistFile(self, obj, extensao):
        ''' cria um arquivo'''
        path = self.pastaDeck+"/"+self.nameDeck+"."+extensao
        if self.it_is_ok(path):
            return False
        else:
            #Criando Arquivo
            arquivo = open(path, 'w')
            arquivo.write(obj)
            arquivo.close()
            return True
    
    def persistDir(self, path):
        ''' Cria o diretorio contido em path '''
        try:
            os.mkdir("./"+path)
            return True
        except:
            return False
   
    def listDeck(self):
        '''Dicionario com todos os Decks'''
        lista = os.listdir("Deck/")
        lista.remove("img")
        dictDeck = {}
        for deck in lista:
            key = deck[5:]
            dictDeck[key]=deck
        return dictDeck
    
    def load(self, extensao):
        '''Abre um arquivo para leitura'''
        path_file = self.pastaDeck+"/"+self.nameDeck+"."+extensao
        file = open(path_file, 'r')
        content = ''
        for line in file:
            content = content + line
        file.close()
        return content

