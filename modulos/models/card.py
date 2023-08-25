from unidecode import unidecode

class Card:

    def __init__(self,qtd,name,url) -> None:
        self.qtd=int(qtd)
        self.name="".join(name.split("/"))
        self.url=url
        self.img=self.nameImg(self.name)

    def json(self):
        return {
            "qtd":self.qtd,
            "name":self.name,
            "url":self.url,
            "img":self.img
        }

    def nameImg(self,nameImg):
        return unidecode( nameImg ).replace(" ","_")