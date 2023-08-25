# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
from ..models.card import Card #Biblioteca para manipular diretorios

class MoxField():
    def __init__(self):
        pass
        
    @staticmethod
    def match(urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('moxfield.') != -1)

    
    def catalogarDeck(self,html):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(html, 'lxml')
        linhas = None
        try:
            row = httpEstruct.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(7) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1)')
            linhas = row.find_all('div', class_="col-auto")
        except:
            print("Deck Inexistente ou privado")
            return

        print("-------------------------")
        #Passa por todas as tabelas (cada tabela é um tipo de carta)
        Deck = {}
        for linha in linhas:
            #Tipo de carta
            nKey = linha.find('span', class_ = 'me-1').text
            if(not nKey in Deck):
                Deck[nKey] = []    
            #Cartas do tipo 'x'
            cartas = linha.find_all('div', attrs={'data-hash': True})
            for carta in cartas:
                name = carta.find('div',class_="decklist-card-phantomsearch").text
                qtd = carta.find('div', class_='decklist-card-quantity show-on-hover').getText()
                qtd = 1 if qtd == 'x' else qtd
                url=carta.find('img').get('src')
                card = Card(qtd,name,url)
                Deck[nKey].append(card.json())
        return Deck