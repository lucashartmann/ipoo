from textual.app import App, ComposeResult
from textual.widgets import Button, Header

# python AppTela.py

class Tela(App):
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Cadastro", id="pressionado")

Tela().run()
