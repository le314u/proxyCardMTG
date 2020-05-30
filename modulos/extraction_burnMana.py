# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
import re #Biblioteca para manipula expressoes regulares
from unidecode import unidecode # Biblioteca para tirar os acentos 

class extraction:
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

    def _name2nameAttribute(self, name):
        #Converte o nome para um nome valido para as propriedades
        nameUnicode = unidecode(name) # Tira os acentos
        nameAttribute = re.sub("( |\([0-9]*\))", "", nameUnicode)
        return nameAttribute
    
    def catalogarDeck(self):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(self.html, 'lxml')

        # verifica se o request ocorreu conforme o esperado
        try:
            deck = httpEstruct.findAll("div", class_= "decklist my-3")
            part_deck = deck.findAll("div", class_= "deck-card-by-list")
            nKey = "";
        except:
            print("Deck Inexistente ou privado")
            return

        #Passa por todos os tipos de cartas
        for kindOfCard in part_deck:
            # Converte o nome para um nome valido para as propriedades
            nameOfKind = kindOfCard.find(class_ = "deck-card-list__type")[0].contents
            nKey = self._name2nameAttribute(nameOfKind)
            # Cada carta é um <li>
            blockOfCards = kindOfCard.findAll("li")
            for card in blockOfCards:
                qtd = card.find("span", class_ = "card-quantity").contents
                detailsCard = card.find("a", class_ = "see-card-image card-detail text-truncate px-1")
                nameOfCard = detailsCard.contents
                urlImg = detailsCard['data-cardimageurl']
                self.Deck[nKey] = []
                if(self.verbose):
                    print("Catalogando :"+nKey+" "*60)
                self.Deck[nKey].append({"qtd":int(qtd),"name":nameOfCard,"url":urlImg,"img":"null"})
        return self.Deck
   