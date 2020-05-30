from modulos import extractionBurnMana, extractionLigaMagic

class extractionManager:
    def __init__(self, verbose=False):
        self.verbose = verbose
        pass

    def selectExtractor(self, urlBase):
        if (self.isLigaMagic(urlBase)):
            extract = extractionLigaMagic.extractionLigaMagic(self.verbose)
        elif (self.isBurnMana):
            extract = extractionBurnMana.extractionBurnMana(self.verbose)
        return extract
    
    def isLigaMagic(self, urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('ligamagic') != -1)
    
    def isBurnMana(self, urlBase):
        urlBase = urlBase.lower()
        return (urlBase.find('burnmana') != -1)