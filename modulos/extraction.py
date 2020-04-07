# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup #Biblioteca de extração de dados
import lxml #Biblioteca parser(analisador) HTML

class extraction:
    def __init__(self,raw):
        self.raw = BeautifulSoup(raw, 'lxml')