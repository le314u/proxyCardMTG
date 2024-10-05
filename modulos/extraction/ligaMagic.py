# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os
from ..models.card import Card #Biblioteca para manipular diretorios
    
class LigaMagic():
    def __init__(self):
        pass
        
    @staticmethod
    def match(urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('ligamagic.') != -1)
    
    def createLink(self,all_img,img):
        return "https://"+all_img.find(id="lazy_"+img).get("lazy-src")[2:]

    def catalogarDeck(self,html):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        Deck = {}
        httpEstruct = BeautifulSoup(html, 'lxml')
        try:
            deck_view = httpEstruct.find(id='deck-view').find(class_='pdeck-block')
            cartas = deck_view.findAll( class_="deck-line")
            nKey = "";
        except:
            print("Deck Inexistente ou privado")
            return
        all_img = httpEstruct.find(id="mystickytooltip")
        currentKey = ''
        currentDeckPart = []
        #Passa por todas as cartas (cada linha é uma carta)
        for carta in cartas:
            # atr = carta.findAll('deck-card',recursive=False)#Pega apenas os filhos diretos
            typeCard = carta.find(class_='deck-type')
            if typeCard is not None:
                key = typeCard.text.split(" ")[0] # Pega o tipo de carta
                Deck[key] = [] # Prepara a Estrutura
                currentDeckPart = Deck[key]
            else:
                nameCard = carta.find(class_='deck-card')
                name = nameCard.text
                qtdCard = carta.find(class_='deck-qty')
                qtd = qtdCard.text
                img = carta.find('a', attrs={'data-tooltip': True}).get("data-tooltip")
                url = self.createLink( all_img,img )
                #Quantidade e nome da carta
                currentDeckPart.append( Card(qtd,name,url).json() )

        return Deck
