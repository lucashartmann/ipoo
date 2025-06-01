from models import Garagem
import App
import ControllerCMD

import sys

garagem = Garagem.Garagem(900)

App.init()
print("Ferroviária 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1:]  # python InterfaceCMD.py ajuda
except IndexError:
    print("ERRO")
    # AgendaController.ctrl_ajuda()
    sys.exit(0)

match comando:
    case ["ajuda"]:
        print(ControllerCMD.ControllerCMD.ajuda())
    case ["adicionar_vagao", peso]:
        ControllerCMD.ControllerCMD.adicionar_vagao(peso)
    case ["adiconar_locomotiva", combustivel, peso]:
        ControllerCMD.ControllerCMD.adicionar_locomotiva(combustivel, peso)
    case ["adicionar_trem"]:
        ControllerCMD.ControllerCMD.adicionar_trem()
    case ["remover", id_veiculo]:
        ControllerCMD.ControllerCMD.remover(id_veiculo)
    case ["engatar", id_trem, id_veiculo]:
        ControllerCMD.ControllerCMD.engatar(id_trem, id_veiculo)
    case ["desengatar", id_trem, id_veiculo]:
        ControllerCMD.ControllerCMD.desengatar(id_trem, id_veiculo)
    case ["esvaziar_garagem_locomotiva"]:
        ControllerCMD.ControllerCMD.remover_locomotivas_da_garagem()
    case ["esvaziar_garagem_vagao"]:
        ControllerCMD.ControllerCMD.remover_vagoes_da_garagem()
    case ["esvaziar_garagem_trem"]:
        ControllerCMD.ControllerCMD.remover_trens_da_garagem()
    case ["esvaziar_trem", id_veiculo]:
        ControllerCMD.ControllerCMD.esvaziar_trem(id_veiculo)
    case ["listar_trens"]:
        print("TRENS NA GARAGEM:")
        print(garagem.get_lista_trens())
    case ["listar_locomotivas"]:
        print("LOCOMOTIVAS NA GARAGEM:")
        print(garagem.get_lista_locomotivas())
    case ["listar_vagoes"]:
        print("VAGÕES NA GARAGEM:")
        print(garagem.get_lista_vagoes())
    case ["listar_veiculos"]:
        veiculos = garagem.get_veiculos_ferroviarios()
        if not veiculos:
            print("Não há veículos na garagem")
        else:
            print("VEÍCULOS NA GARAGEM:")
            for veiculo in veiculos:
                print(veiculo)
    case _:
        print("Entrada inválida")
        print(ControllerCMD.ControllerCMD.ajuda())
