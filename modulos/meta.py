from modulos.extraction.extraction import Extraction
from urllib.parse import urlparse
import json

class Meta:
    def __init__(self) -> None:
        pass

    def loadFile(self,persistence):
        meta = json.loads(persistence.load("meta"))
        scraper = Extraction.select(meta["extractor"])
        return {
                "meta":meta,
                "scraper":scraper,
        }
        
    def dumpMETA(self,persistence,meta):
        prettyMeta = str( json.dumps(meta, indent=4, sort_keys=True) )
        #Persiste os meta dados
        persistence.persistFile( prettyMeta, "meta")
        
    def meta(self,url):
        #Extrai metadados da url
        keyDeck = url.split("/")[-1].split("=")[-1]
        site = urlparse(url).hostname
        #Cria um Objeto para ser salvo
        meta = { "nameDeck":keyDeck, "dirDeck":"Deck/deck_"+keyDeck, "extractor":site, "url":url }
        scraper = Extraction.select(meta["extractor"])
        return {
            "meta":meta,
            "scraper":scraper,
        }
        
        
    

