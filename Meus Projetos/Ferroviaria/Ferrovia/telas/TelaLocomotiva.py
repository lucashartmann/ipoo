from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll, Vertical, Horizontal
from textual.widgets import Button, Footer, Header, TextArea, Label, Checkbox, Input
from controller.ControllerCMD import ControllerCMD
from textual.screen import Screen

# python -m telas.TelaInicial


class TelaLocomotiva(Screen):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            peso = float(self.query_one("#input_peso_locomotiva", Input).value)
            combustivel = float(self.query_one(
                "#input_combustivel_locomotiva", Input).value)
            mensagem = ControllerCMD.adicionar_locomotiva(combustivel, peso)
            areaTexto = self.screen.query_one("#mensagem", TextArea)
            areaTexto.text = mensagem

        elif event.button.id == "trocar_tela":
            self.screen.app.pop_screen()

    CSS_PATH = "../css/Telas.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield HorizontalGroup(
            Vertical(
                Label("Digite a quantidade de combustível da locomotiva:",
                      id="label_combustivel_locomotiva"),
                Label("Digite o peso da locomotiva:",
                      id="label_peso_locomotiva"),
            ),
            Vertical(
                Input("Digite aqui", id="input_combustivel_locomotiva"),
                Input("Digite aqui", id="input_peso_locomotiva"),
                Button("Cadastrar", id="cadastrar"),
                Button("Voltar", id="trocar_tela"),
            ),
        )
        yield HorizontalGroup(
            Checkbox("Gasolina", id="gasolina"),
            Checkbox("Vapor", id="vapor"),
            Checkbox("Bateria", id="bateria"),
        )
        yield TextArea(id="mensagem", disabled=True)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
