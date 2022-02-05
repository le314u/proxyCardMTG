# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios

    
class MoxField:
    def __init__(self, verbose=False):
        self.Deck = {}
        self.html = None
        self.nameDeck = ''
        self.pastaDeck = ''
        self.verbose = verbose

    def load(self, html, nameDeck, pastaDeck):
        self.Deck = {}
        self.html=html
        self.nameDeck=nameDeck
        self.pastaDeck=pastaDeck

    
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
   