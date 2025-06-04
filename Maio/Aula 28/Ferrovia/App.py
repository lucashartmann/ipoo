from models import Locomotiva, Vagao, Trem, Garagem
import Controller
import View

Controller.Controller.init()


def menu():
    while True:
        View.View.ver_menu()
        opcao = int(View.View.pedir_dados("Digite o número da opção desejada"))
        match opcao:
            case 1 | 2 | 3:
                Controller.Controller.cadastro(opcao)
            case 4 | 5 | 6:
                Controller.Controller.remocao(opcao)
            case 7:
                Controller.Controller.engatar_no_trem()
            case 8:
                Controller.Controller.desengatar()
            case 9:
                Controller.Controller.esvaziar_garagem()
            case 10:
                Controller.Controller.esvaziar_trem()
            case 11:
                Controller.Controller.listar_vagoes_garagem()
            case 12:
                Controller.Controller.listar_locomotivas_garagem()
            case 13:
                Controller.Controller.listar_trens_garagem()
            case 14:
                Controller.Controller.listar_veiculos_garagem()
            case 15:
                Controller.Controller.get_quant_veiculos_na_garagem()
            case 16:
                break
            case _:
                View.View.mostrar_mensagem("Opção inválida, tente novamente")


if __name__ == "__main__":
    View.View.mostrar_mensagem(
        "Ferroviária 2025 - v.0.1.0 - SENAC Tech - POA/RS")
    menu()
    View.View.mostrar_mensagem("Programa encerrado.")
