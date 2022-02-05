# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
from .extractor import Extractor
    
class MoxField(Extractor):
    def __init__(self, verbose=False):
        super().__init__(verbose);

    def load(self, html, nameDeck, pastaDeck):
        super().load(html, nameDeck, pastaDeck);
        
    @staticmethod
    def thisExtractor(urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('moxfield.') != -1)

    
    def catalogarDeck(self):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(self.html, 'lxml')
        try:
            tabelas = httpEstruct.findAll('table')
        except:
            print("Deck Inexistente ou privado")
            return

        
        #Passa por todas as tabelas (cada tabela é um tipo de carta)
        for tabela in tabelas:
            nKey = tabela.find('tr').find('a').contents[1].split(' ')[1]
            if(not nKey in self.Deck):
                self.Deck[nKey] = []
                tabela.find('tbody')
                linhas = tabela.find('tbody').findAll('tr')
                #Passa por todas as cartas (cada linha é uma carta)
                for linha in linhas:
                    colunas = linha.findAll('td',recursive=False)#Pega apenas os filhos diretos
                    qtd = colunas[0].text
                    name = colunas[1].text
                    img = linha["data-hash"]#Style css é o nome do arquivo
                    url = "assets.moxfield.net/cards/card-"+img+"-normal.webp"
                    #Quantidade e nome da carta
                    self.Deck[nKey].append({"qtd":int(qtd),"name":name,"url":url,"img":img})
        return self.Deck