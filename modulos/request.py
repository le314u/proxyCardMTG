# -*- encoding: utf-8 -*-
import requests as r

class requests:
    def __init__(self,url):
        #Preparando para pegar o conteudo da pagina web
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        #Pega o conteudo da pagina web
        self.response = r.get(url, headers=self.headers)

