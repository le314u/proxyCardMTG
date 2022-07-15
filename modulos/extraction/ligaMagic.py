# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML
import os #Biblioteca para manipular diretorios
from .extractor import Extractor
    
class LigaMagic(Extractor):
    def __init__(self, verbose=False):
        super().__init__(verbose);

    def load(self, html, nameDeck, pastaDeck):
        super().load(html, nameDeck, pastaDeck);
        
    @staticmethod
    def thisExtractor(urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('ligamagic.') != -1)
    
    
    def catalogarDeck(self):
        '''Cataloga o Deck (pegando [qtd, nome, img, css])'''
        httpEstruct = BeautifulSoup(self.html, 'lxml')
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
                    if(self.verbose):
                        print("Deck Completo"+colunas[0].contents[0]+" "*60)
                        break
                else:
                    #label que define o tipo da carta (criatura, artefato,magica)
                    nKey = colunas[0].contents[0].replace(" ","",-1)
                    self.Deck[nKey] = []
                    if(self.verbose):
                        print("Catalogando :"+nKey+" "*60)

            else:
                qtd = int(colunas[0].string)
                name = colunas[1].findNext('a').getText()
                img = linha.find("a")["data-tooltip"]#Style css é o nome do arquivo
                url = httpEstruct.find_all(id="mystickytooltip")[0].find(id="lazy_"+img)['lazy-src'][2:]
        
                #Quantidade e nome da carta
                self.Deck[nKey].append({"qtd":int(qtd),"name":name,"url":url,"img":img})
        return self.Deck
