import os

class View:

    @staticmethod  
    def listOptions():
        return {
            "Exemplo":"Cria um arquivo de modelo",
            "New":"Cria um novo deck",
            "Old":"Cria um deck ja existente"
        }

    @staticmethod  
    def listDecks():
        '''Dicionario com todos os Decks'''
        lista = os.listdir("Deck/")
        lista.remove("img")
        dictDeck = {}
        for deck in lista:
            key = deck[5:]
            dictDeck[key]=deck
        return dictDeck