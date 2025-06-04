from models import Garagem
import App
import ControllerCMD
import sys
import View


View.View.mostrar_mensagem(
    "Ferroviária 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1:]  # python InterfaceCMD.py ajuda
except IndexError:
    View.View.mostrar_mensagem("ERRO")
    View.View.ajuda()
    sys.exit(0)

match comando:
    case ["ajuda"]: # python InterfaceCMD.py ajuda
        View.View.ajuda()
    case ["adicionar_vagao", peso]: # python InterfaceCMD.py adicionar_vagao 100.0
        ControllerCMD.ControllerCMD.adicionar_vagao(peso)
    case ["adicionar_locomotiva", combustivel, peso]: # python InterfaceCMD.py adicionar_locomotiva 100.0 500.0
        ControllerCMD.ControllerCMD.adicionar_locomotiva(combustivel, peso)
    case ["adicionar_trem"]: # python InterfaceCMD.py adicionar_trem
        ControllerCMD.ControllerCMD.adicionar_trem()
    case ["remover", id_veiculo]: # python InterfaceCMD.py remover 1
        ControllerCMD.ControllerCMD.remover(id_veiculo)
    case ["engatar", id_trem, id_veiculo]: # python InterfaceCMD.py engatar 1 2
        ControllerCMD.ControllerCMD.engatar(id_trem, id_veiculo)
    case ["desengatar", id_trem, id_veiculo]: # python InterfaceCMD.py desengatar 1 2
        ControllerCMD.ControllerCMD.desengatar(id_trem, id_veiculo)
    case ["esvaziar_garagem_locomotiva"]: # python InterfaceCMD.py esvaziar_garagem_locomotiva
        ControllerCMD.ControllerCMD.remover_locomotivas_da_garagem()
    case ["esvaziar_garagem_vagao"]: # python InterfaceCMD.py esvaziar_garagem_vagao
        ControllerCMD.ControllerCMD.remover_vagoes_da_garagem()
    case ["esvaziar_garagem_trem"]: # python InterfaceCMD.py esvaziar_garagem_trem
        ControllerCMD.ControllerCMD.remover_trens_da_garagem()
    case ["esvaziar_trem", id_veiculo]: # python InterfaceCMD.py esvaziar_trem 1
        ControllerCMD.ControllerCMD.esvaziar_trem(id_veiculo)
    case ["listar_trens"]: # python InterfaceCMD.py listar_trens
        ControllerCMD.ControllerCMD.listar_trens()
    case ["listar_locomotivas"]: # python InterfaceCMD.py listar_locomotivas
        ControllerCMD.ControllerCMD.listar_locomotivas()
    case ["listar_vagoes"]: # python InterfaceCMD.py listar_vagoes
        ControllerCMD.ControllerCMD.listar_vagoes()
    case ["listar_veiculos"]: # python InterfaceCMD.py listar_veiculos
        ControllerCMD.ControllerCMD.listar_veiculos()
    case _:
        View.View.mostrar_mensagem("Entrada inválida")
        View.View.ajuda()
