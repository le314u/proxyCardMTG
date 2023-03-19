# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
    
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
            linhas = httpEstruct.tbody.findAll('tr')
            nKey = "";
        except:
            print("Deck Inexistente ou privado")
            return

        #Passa por todas as cartas (cada linha é uma carta)
        for linha in linhas:
            colunas = linha.findAll('td',recursive=False)#Pega apenas os filhos diretos
            if len(colunas) == 1:
                if len(colunas[0].contents) == 1:
                    #Chegou ao fim onde informa o total de cartas
                    print("Deck Completo"+colunas[0].contents[0]+" "*60)
                else:
                    #label que define o tipo da carta (criatura, artefato,magica)
                    nKey = colunas[0].contents[0].replace(" ","",-1)
                    Deck = {}
                    Deck[nKey] = []
                    print("Catalogando :"+nKey+" "*60)

            else:
                qtd = int(colunas[0].string)
                name = colunas[1].findNext('a').getText()
                img = linha.find("a")["data-tooltip"]#Style css é o nome do arquivo
                url = httpEstruct.find_all(id="mystickytooltip")[0].find(id="lazy_"+img)['lazy-src'][2:]
        
                #Quantidade e nome da carta
                Deck[nKey].append({"qtd":int(qtd),"name":name,"url":url,"img":img})
        return Deck
