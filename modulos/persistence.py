from pathlib import Path
import os
class persistence:

    def __init__(self):
        self.nameDeck = ''
        self.pastaDeck = ''

    def processeUrl(self, url):
        '''Define pasta onde ira persistir as imagens do deck'''
        self.nameDeck = url.split("/")[-1].split("=")[-1]
        self.pastaDeck = "deck_"+self.nameDeck

        return (self.nameDeck, self.pastaDeck)
    
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

    def load(self, extensao):
        path_file = self.pastaDeck+"/"+self.nameDeck+"."+extensao
        file = open(path_file, 'r')
        content = ''
        for line in file:
            content = content + line
        file.close()
        return content
