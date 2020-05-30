# -*- encoding: utf-8 -*-
import requests #Biblioteca que faz requisições http
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
from . import persistence
class request:

    def __init__(self, verbose=True):
        #Cabeçalho de requisição get
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        self.verbose=verbose

    def downloadHTML(self, url):
        #Faz download da pagina
        if(self.verbose):
            print("Acessando pagina: "+url)
        httpRequest = requests.get(url, headers=self.headers)
        return httpRequest.text
    
    def downloadIMG(self, url, nameArq):
        if(self.verbose):
            print("Fazendo download de: "+url,end=" "*60+"\r")
        binImg = requests.get(url, headers=self.headers)
        open(nameArq,'wb').write(binImg.content)