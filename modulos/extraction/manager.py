from .burnMana import BurnMana
from .ligaMagic import LigaMagic
from .moxField import MoxField
from .tappedout import Tappedout

class Manager:
    def __init__(self, verbose=True):
        self.verbose = verbose
        pass

    def selectExtractor(self, urlBase):
        if(LigaMagic.thisExtractor(urlBase)):
            extract = LigaMagic(self.verbose)
        elif (BurnMana.thisExtractor(urlBase)):
            extract = BurnMana(self.verbose)
        elif (MoxField.thisExtractor(urlBase)):
            extract = MoxField(self.verbose)
        elif (Tappedout.thisExtractor(urlBase)):
            extract = Tappedout(self.verbose)
        return extract
        