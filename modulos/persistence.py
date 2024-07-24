from pathlib import Path
import os
from unicodedata import name
from urllib.parse import urlparse
from .msg import msg


class Persistence:

    def __init__(self):
        self.DIR="Deck/"
        self.PREFIX="deck_"
        #Atributos
        self.nameDeck = ''
        self.pastaDeck = ''
        try:#Cria as pastas essenciais para que o programa funcione
            self.persistDir("Deck")
            self.persistDir("Deck/img")
        except:
            pass

    def path(self, nameDeck):
        '''Carrega os metaDados de um deck'''
        self.nameDeck = nameDeck
        self.pastaDeck = "./"+self.DIR+self.PREFIX+nameDeck


    def setupDeck(self,nameDeck):
        self.path(nameDeck)
        # Verifica se existe um diretorio proprio para o deck
        if not self.it_is_ok(self.pastaDeck):
            #Cria o diretorio que ficara todos os arquivos do deck
            if(not self.persistDir(self.pastaDeck)):
                print("Erro ao criar Diretorio")

    def processOk(self, extensao):
        ''' Verifica o que ja foi feito '''
        #Arquivo esta ok?
        value = self.it_is_ok(self.pastaDeck+"/"+self.nameDeck+"."+extensao)
        msg(extensao.upper(),value)
        return value

    def it_is_ok(self, path):
        ''' Verifica se existe um arquivo de acordo com o path '''
        file = Path(path)
        return (file.is_file() or file.is_dir())

    def persistDir(self, path):
        ''' Cria o diretorio contido em path '''
        try:
            os.mkdir("./"+path)
            return True
        except:
            return False

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
    
    def load(self, extensao):
        '''Abre um arquivo para leitura'''
        path_file = self.pastaDeck+"/"+self.nameDeck+"."+extensao
        file = open(path_file, 'r')
        content = ''
        for line in file:
            content = content + line
        file.close()
        return content

