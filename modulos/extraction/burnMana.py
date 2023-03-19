# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
import re #Biblioteca para manipula expressoes regulares
from unidecode import unidecode # Biblioteca para tirar os acentos 

class BurnMana():
    def __init__(self):
      pass
    
    @staticmethod
    def match(urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('burnmana.') != -1)

    def _name2nameAttribute(self, name):
        #Converte o nome para um nome valido para as propriedades
        nameUnicode = unidecode(name) # Tira os acentos
        nameAttribute = re.sub("( |\([0-9]*\))", "", nameUnicode)
        return nameAttribute
    
    def _nameCard(self, name):
        nameCard = re.sub("(\\n|\\t)", "", name)
        return nameCard

    def _removeProtocol(self, uri):
        url = re.sub("^https://", "", uri)
        return url

    def catalogarDeck(self,html):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(html, 'lxml')

        # verifica se o request ocorreu conforme o esperado
        try:
            deck = httpEstruct.find("div", class_= "decklist my-3")
            part_deck = deck.findAll("div", class_= "deck-card-by-list")
            nKey = "";
        except:
            print("Deck Inexistente ou privado")
            return
        #Passa por todos os tipos de cartas
        for kindOfCard in part_deck:
            # Converte o nome para um nome valido para as propriedades
            nameOfKind = kindOfCard.find(class_ = "deck-card-list__type").contents[0]
            nKey = self._name2nameAttribute(nameOfKind)
            Deck = {}
            Deck[nKey] = []
            # Cada carta é um <li>
            blockOfCards = kindOfCard.findAll("li")
            for card in blockOfCards:
                qtd = card.find("span", class_ = "card-quantity").contents[0]
                detailsCard = card.find("a", class_ = "see-card-image card-detail text-truncate px-1")
                nameOfCard = self._nameCard(detailsCard.contents[0])
                urlImg = self._removeProtocol(detailsCard['data-cardimageurl'])
                nameImg = urlImg.split('/')[-1]
                print("Catalogando : "+nKey+" "*60)
                Deck[nKey].append({
                        "qtd":int(qtd),
                        "name":nameOfCard,
                        "url":urlImg,
                        "img":nameImg
                    })
        return Deck