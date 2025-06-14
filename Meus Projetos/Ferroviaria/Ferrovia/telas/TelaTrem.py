from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header, TextArea, Label
from controller.ControllerCMD import ControllerCMD
from textual.screen import Screen
from textual.events import MouseEvent, MouseCapture, MouseDown

# python -m telas.TelaInicial


class TelaCadastroTrem(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "engatar":
            mensagem = "LUCASASDASDSPAJDIOPASJPDJPASOJDPJSOJDSOPDJAS"
            areaTexto = self.screen.query_one("#textArea_Trem", TextArea)
            areaTexto.text += mensagem

        if event.button.id == "trocar_tela":
            self.screen.app.pop_screen()

    def definir_locomotivas(self):
        lista_locomotivas = ControllerCMD.listar_locomotivas_garagem()
        areaLocomotivas = self.screen.query_one(
            "#textArea_trem_locomotivas", TextArea)
        areaLocomotivas.text = lista_locomotivas

    def definir_vagoes(self):
        lista_vagoes = ControllerCMD.listar_vagoes_garagem()
        areaVagoes = self.screen.query_one("#textArea_trem_vagoes", TextArea)
        areaVagoes.text = lista_vagoes

    def compose(self) -> ComposeResult:
        self.definir_locomotivas()
        self.definir_vagoes()
        yield Button("Criar Trem", id="cadastrar")
        yield Button("Engatar no Trem", id="engatar")
        yield Button("Voltar", id="trocar_tela")


class TelaTrem(Screen):

    CSS_PATH = "../css/Telas.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(TelaCadastroTrem())
        yield TextArea(id="textArea_trem_locomotivas", disabled=True)
        yield TextArea(id="textArea_trem_vagoes", disabled=True)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
