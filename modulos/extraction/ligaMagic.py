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
    
    
    def catalogarDeck(self,html):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(html, 'lxml')
        try:
            cartas = httpEstruct.tbody.findAll('tr')
            nKey = "";
        except:
            print("Deck Inexistente ou privado")
            return

        Deck = {}
        #Passa por todas as cartas (cada linha é uma carta)
        for carta in cartas:
            atr = carta.findAll('td',recursive=False)#Pega apenas os filhos diretos
            if len(atr) == 1:
                if len(atr[0].contents) == 1:
                    #Chegou ao fim onde informa o total de cartas
                    print("Deck Completo"+atr[0].contents[0]+" "*60)
                else:
                    #label que define o tipo da carta (criatura, artefato,magica)
                    nKey = carta.find('td',class_="deck-type").getText().split(" ")[0]
                    Deck[nKey] = []
                    print("Catalogando :"+nKey+" "*60)
            else:
                qtd = carta.find('td',class_="deck-qty").string
                name = carta.find('td',class_="deck-card").find('a').getText()
                img = carta.find('a', attrs={'data-tooltip': True}).get("data-tooltip")
                all_img = httpEstruct.find(id="mystickytooltip")
                url = all_img.find(id="lazy_"+img).get("lazy-src")[2:]
                #Quantidade e nome da carta
                card = Card(qtd,name,url)
                Deck[nKey].append(card.json())
        print(Deck)
        return Deck
