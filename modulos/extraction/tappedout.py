# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
from lxml import etree
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
    
class Tappedout():
    def __init__(self):
        pass
        
    @staticmethod
    def match(urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('tappedout.') != -1)

    
    def catalogarDeck(self,html):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(html, 'lxml')
        try:
            tabelas = httpEstruct.findAll('div','row board-container')
        except:
            print("Deck Inexistente ou privado")
            return
        Deck = {}
        #Passa por todas as tabelas (main e side)
        for tabela in tabelas:
            colunas = tabela.findAll('div', 'board-col col-md-4 col-sm-12')
            for coluna in colunas:
                titulos = coluna.findAll('h3')
                cards = coluna.findAll('ul')
                for i in range(len(titulos)):
                    nKey = titulos[i].text.split('(')[0][0:-1]
                    if not nKey in Deck:
                        Deck[nKey] = []
                    #Passa por todas as cartas (cada linha é uma carta)
                    for card in cards[i].findAll('li'):
                        tagCard1 =  card.find('a')
                        tagCard2 =  card.find('span').find('a')
                        name = tagCard1['data-orig']
                        qtd = tagCard1['data-qty']
                        img = tagCard2['data-name']#nome da img
                        url = tagCard2['data-image'][2:]#link da img
                        #Quantidade e nome da carta
                        Deck[nKey].append({"qtd":int(qtd),"name":name,"url":url,"img":img})
        return Deck
