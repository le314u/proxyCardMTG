class Extractor():
    def __init__(self, verbose):
        self.Deck = {}
        self.html = None
        self.nameDeck = ''
        self.pastaDeck = ''
        self.verbose = verbose

    def load(self, html, nameDeck, pastaDeck):
        self.Deck = {}
        self.html=html
        self.nameDeck=nameDeck
        self.pastaDeck=pastaDeck