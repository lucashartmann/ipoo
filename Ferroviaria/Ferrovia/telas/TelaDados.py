from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Header, Footer, TextArea
from textual.screen import Screen
from controller.ControllerCMD import ControllerCMD


class WidgetsDados(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed):
        areaTexto = self.screen.query_one("#resultado", TextArea)
        match event.button.id:
            case "locomotivas_garagem":
                str_lista = ControllerCMD.listar_locomotivas_garagem()
                str_quant = ControllerCMD.get_quant_locomotivas_garagem()
                str_final = str_quant + "\n" + str_lista
                areaTexto.text = str_final
            case "vagoes_garagem":
                str_lista = ControllerCMD.listar_veiculos_garagem()
                str_quant = ControllerCMD.get_quant_veiculos_garagem()
                str_final = str_quant + "\n" + str_lista
                areaTexto.text = str_final
            case "trens_garagem":
                str_lista = ControllerCMD.listar_trens_garagem()
                str_quant = ControllerCMD.get_quant_trens_garagem()
                str_final = str_quant + "\n" + str_lista
                areaTexto.text = str_final
            case "veiculos_garagem":
                str_lista = ControllerCMD.listar_veiculos_garagem()
                str_quant = ControllerCMD.get_quant_veiculos_garagem()
                str_final = str_quant + "\n" + str_lista
                areaTexto.text = str_final
            case "locomotivas_trem":
                str_lista = ControllerCMD.listar_locomotivas_garagem()
                str_quant = ControllerCMD.get_quant_locomotivas_garagem()
                str_final = str_quant + "\n" + str_lista
                areaTexto.text = str_final
            case "vagoes_garagem":
                str_lista = ControllerCMD.listar_vagoes_garagem()
                str_quant = ControllerCMD.get_quant_vagoes_garagem()
                str_final = str_quant + "\n" + str_lista
                areaTexto.text = str_final

    def compose(self) -> ComposeResult:
        yield Button("Locomotivas na garagem", id="locomotivas_garagem")
        yield Button("Vagões na garagem", id="vagoes_garagem")
        yield Button("Trens na garagem", id="trens_garagem")
        yield Button("Todos os veiculos na garagem", id="veiculos_garagem")
        yield Button("Locomotivas no trem", id="locomotivas_trem")
        yield Button("Vagões no trem", id="vagoes_trem")


class TelaDados(Screen):
    CSS_PATH = "../css/Telas.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(WidgetsDados())
        yield TextArea(id="resultado")
        yield Footer()
