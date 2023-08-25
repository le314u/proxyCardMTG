import json

class Deck:

    def __init__(self) -> None:
        pass

    def loadFile(self,persistence):
        return json.loads(persistence.load("deck"))

    def create(self,scraper,html):
        deck = scraper.catalogarDeck(html)
        return deck

    def dumpDECK(self,persistence,deck):
        #Persiste o Deck
        prettyDeck = str( json.dumps(deck, indent=4, sort_keys=False) )
        persistence.persistFile( prettyDeck, "deck")

    def dumpIMG(self,request,persistence,deck):
        listUrl = []
        #Preparando para trabalhar com o deck
        print("Cards:")
        for type in deck:
            cards = deck[type]
            for card in cards:
                msg = str(card["qtd"])+" "+str(card['name'])
                print( msg)
                listUrl.append(card['url'])
                #Faz Download da imagem
                url = card['url']
                name = "Deck/img/"+card['img']+'.jpg'
                #Verifica se a imagem ja existe
                if(not persistence.it_is_ok(name)):
                    request.downloadIMG(url, name)
        persistence.persistFile("\n".join(listUrl), "img")