import os
import webbrowser
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, Input, Label, ListItem, ListView, OptionList
from textual.reactive import reactive
from textual import on

def listDecks():
        '''Dicionario com todos os Decks'''
        lista = os.listdir("Deck/")
        lista.remove("img")
        lint = lambda name: name[5:]
        decks =  list(map(lint, lista))
        return decks

def getDeck(id):
    return listDecks()[id]

def open(path):
    caminho = os.path.realpath(path)  # Garante que o caminho esteja formatado corretamente
    url = 'file:///' + caminho.replace('\\', '/')  # Converte o caminho para URL
    webbrowser.open(url)

def labelDeck():
    options= self.query_one("#options")
    deck = str(getDeck(options.highlighted))
    return deck
    

class State(Static):
    """A widget to display elapsed time."""

class LineUrl(Static):
    """LineUrl widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Get", id="get", variant="success")
        yield Input(placeholder="URL",id="url")

class LineDeck(Static):
    """LineDeck widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Set", id="set", variant="success")
        yield OptionList(*listDecks(),id="options" )
        
class View(App):
    """A Textual app to manage stopwatches."""
    TITLE="ProxyCardMTG"
    BINDINGS = [
        ("p", "pdf", "PDF do Deck" ),
        ("q", "exit", "Exit" ),
        ("m", "meta", "Abre o metaDado" ),
        #("d", "deck", "Abre o Deck" ),
    ]
    CSS_PATH = "style.tcss"

  
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield LineUrl()
        yield LineDeck()
        yield Footer()
        # yield ScrollableContainer(LineUrl(),LineDeck())

    def labelDeck(self):
        options= self.query_one("#options")
        deck = str(getDeck(options.highlighted))
        return deck

    def action_exit(self) -> None:
        exit(1)

    def action_pdf(self) -> None:
        deck = self.labelDeck()
        path = f'./Deck/deck_{deck}/{deck}.pdf'
        open(path)

    def action_deck(self) -> None:
        deck = self.labelDeck()
        path = f'./Deck/deck_{deck}/{deck}.deck'
        open(path)
    
    def action_meta(self) -> None:
        deck = self.labelDeck()
        path = f'./Deck/deck_{deck}/{deck}.meta'
        open(path)

    def setConf(self,flow, setConfig,state):
        self.setConfig = setConfig
        self.state = state
        self.flow = flow

    @on(Input.Submitted)
    def setUrl(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        try:
            input= self.query_one("#url")
            url = input.value
            self.flow( url )
            deck = url.split("/")[-1].split("=")[-1]
            path = f'./Deck/deck_{deck}/{deck}.pdf'
            open(path)
        except:
            pass

    @on(Button.Pressed, "#get")
    def clickGet(self, event: Button.Pressed) -> None:
        # Set URL
        if event.button.id == "get":
            self.setUrl(event)
            
    @on(Button.Pressed, "#set")
    def clickSet(self, event: Button.Pressed) -> None:
        #Set Code
        if event.button.id == "set":
            options= self.query_one("#options")
            deck = str(getDeck(options.highlighted))
            self.setConfig(deck)     
            self.flow()
            path = f'./Deck/deck_{deck}/{deck}.pdf'
            open(path)
