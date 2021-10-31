from . import burnMana, ligaMagic, moxField

class Manager:
    def __init__(self, verbose=True):
        self.verbose = verbose
        pass

    def selectExtractor(self, urlBase):
        if (self.isLigaMagic(urlBase)):
            extract = ligaMagic.LigaMagic(self.verbose)
        elif (self.isBurnMana(urlBase)):
            extract = burnMana.BurnMana(self.verbose)
        elif (self.isMoxField(urlBase)):
            extract = moxField.MoxField(self.verbose)
        return extract
        
    def isLigaMagic(self, urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('ligamagic.') != -1)
    
    def isBurnMana(self, urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('burnmana.') != -1)
    
    def isMoxField(self, urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('moxfield.') != -1)
