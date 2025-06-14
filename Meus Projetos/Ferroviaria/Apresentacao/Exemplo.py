from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer
from textual.screen import Screen

# python Exemplo.py

class SegundaTela(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


class Tela(App):

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "pressionado":
            self.app.push_screen(SegundaTela())

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Cadastro", id="pressionado")


Tela().run()
