from .burnMana import BurnMana
from .ligaMagic import LigaMagic
from .moxField import MoxField
from .tappedout import Tappedout

class Extraction:
    
    @staticmethod
    def select(urlBase):
        extract = None;
        if(LigaMagic.match(urlBase)):
            extract = LigaMagic()
        elif (BurnMana.match(urlBase)):
            extract = BurnMana()
        elif (MoxField.match(urlBase)):
            extract = MoxField()
        elif (Tappedout.match(urlBase)):
            extract = Tappedout()
        return extract
        