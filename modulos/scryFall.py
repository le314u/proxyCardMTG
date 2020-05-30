import urllib.parse #Biblioteca para codificar URL
import requests #Biblioteca que faz requisições http

class scryfall:
    def __init__():
        baseUriImg = "https://api.scryfall.com/cards/"
        baseUriName = "https://api.scryfall.com/cards/named?fuzzy="
        langOpt = {
            "Inglês":"en",
            "Espanhol":"es",
            "Francês":"fr",
            "Alemão":"de",
            "Italiano":"it",
            "Português":"pt",
            "Japonês":"ja",
            "Coreano":"ko",
            "Russo":"ru",
            "Chinês simplificado":"zhs",
            "Chinês tradicional":"zht"
        }

    def encodeURI(query):
        return urllib.parse.quote(query)

    def extractData(cardJson):
        cardJson['set']
        cardJson['collector_number']

    def makeUriName(name):
        return baseUriName + self.encodeURI(name)

    def makeUriImg(set, cod, lang):
        return baseUriImg + set + "/" + cod + "/" + lang + "?format=image&version=border_crop"