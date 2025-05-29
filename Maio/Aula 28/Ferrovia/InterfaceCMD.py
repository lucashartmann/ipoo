import App
import Locomotiva
import Vagao
import Trem
import Garagem

import sys

garagem = Garagem.Garagem(900)

App.init()
print("Ferroviária 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1]  # python InterfaceCMD.py listar
except IndexError:
    print("ERRO")
    # AgendaController.ctrl_ajuda()
    sys.exit(0)

comando = comando.lower()

match comando:
    case ["ajuda"]:
        ajuda()
    case ["adicionar_vagao", peso]:
        adicionar_vagao(peso)
    case ["adiconar_locomotiva", combustivel, peso]:
        adicionar_locomotiva(combustivel, peso)
    case ["adicionar_trem"]:
        adicionar_trem()
    case ["remover", id_veiculo]:
        remover(id_veiculo)
    case ["engatar", id_trem, id_veiculo]:
        engatar(id_trem, id_veiculo)
    case ["desengatar", id_trem, id_veiculo]:
        desengatar(id_trem, id_veiculo)
    case ["esvaziar_garagem_locomotiva"]:
        pass
    case ["esvaziar_garagem_vagao"]:
        pass
    case ["esvaziar_garagem_trem"]:
        pass
    case ["esvaziar_trem", id_veiculo]:
        pass
    case _:
        print("Entrada inválida")
        # help()


def ajuda():
    comandos = '''
    Comandos para a execução do programa:

    "adicionar_vagao peso" -> exemplo: "adicionar_vagao 600.00"
    "adiconar_locomotiva combustivel peso" -> exemplo: "adiconar_locomotiva 500.30 1000.5"
    "adicionar_trem"
    "remover id_trem id_veiculo" -> exemplo: "remover 1 4"
    "engatar id_trem id_veiculo" -> exemplo: "engatar 1 3"
    "desengatar id_trem id_veiculo" -> exemplo: "desengatar 1 2"
    "esvaziar_garagem_locomotiva" 
    "esvaziar_garagem_vagao"
    "esvaziar_garagem_trem"
    "esvaziar_trem id_veiculo" -> exemplo: "esvaziar_trem 1"
    "ajuda"
    '''
    print(comandos)


def adicionar_vagao(peso):
    vagao = Vagao.Vagao(peso)
    cadastro = garagem.estacionar(vagao)
    if cadastro:
        print("Cadastro realizado com sucesso")
        print(vagao)
    else:
        print("ERRO. Não foi possivel realizar cadastro")


def adicionar_locomotiva(combustivel, peso):
    locomotiva = Locomotiva.Locomotiva(combustivel, peso)
    cadastro = garagem.estacionar(locomotiva)
    if cadastro:
        print("Cadastro realizado com sucesso")
        print(locomotiva)
    else:
        print("ERRO. Não foi possivel realizar cadastro")


def adicionar_trem():
    trem = Trem()
    cadastro = garagem.estacionar(trem)
    if cadastro:
        print("Cadastro realizado com sucesso")
        print(trem)
    else:
        print("ERRO. Não foi possivel realizar cadastro")


def remover(id):
    veiculo = garagem.get_veiculo_por_id(id)
    remocao = garagem.remove_veiculo(veiculo)
    if remocao:
        print(veiculo, "removido com sucesso")
    else:
        print("ERRO. Não foi possivel remover", veiculo)


def engatar(id_trem, id_veiculo):
    trem = garagem.get_veiculo_por_id(id_trem)
    if trem is None:
        print(f"Não existe trem com o id: {id_trem}")
        return
    else:
        veiculo = garagem.get_veiculo_por_id(id_veiculo)
        if type(veiculo) == Vagao.Vagao:
            if trem.possui_locomotiva() == False:
                print("ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
                return
        if veiculo is None:
            print(f"Não existe veiculo com o id: {id_veiculo}")
            return
        engatado = trem.engatar(veiculo)
        if engatado:
            garagem.remove_veiculo(veiculo)
            print(veiculo, "engatado com sucesso!")
        else:
            print("ERRO ao engatar", veiculo)


def desengatar(id_trem, id_veiculo):
    trem = garagem.get_veiculo_por_id(id_trem)
    if trem is None:
        print(f"Não existe trem com o id: {id_trem}")
        return
    veiculo = garagem.get_veiculo_por_id(id_veiculo)
    if veiculo is None:
        print(f"Não existe veiculo com o id: {id_veiculo}")
        return
    desengatado = trem.desengatar(veiculo)
    if desengatado:
        garagem.estacionar(veiculo)
        print(veiculo, "desengatado com sucesso!")
    else:
        print("ERRO ao desengatar", veiculo)


def remover_trens_da_garagem():
    garagem.remover_todos_trens()
    print("Trens removidos com sucesso")
    print("TRENS NA GARAGEM:")
    print(garagem.get_lista_trens())


def remover_locomotivas_da_garagem():
    garagem.remover_todas_locomotivas()
    print("Locomotivas removidass com sucesso")
    print("LOCOMOTIVAS NA GARAGEM:")
    print(garagem.get_lista_locomotivas())


def remover_vagoes_da_garagem():
    garagem.remover_todos_vagoes()
    print("Vagões removidos com sucesso")
    print("VAGÕES NA GARAGEM:")
    print(garagem.get_lista_vagoes())


def esvaziar_trem(id):
    trem = garagem.get_veiculo_por_id(id_trem)
    if trem is None:
        print(f"Não existe trem com o id: {id_trem}")
        return
    trem.esvaziar()
    print("Trem esvaziado com sucesso!", trem)
