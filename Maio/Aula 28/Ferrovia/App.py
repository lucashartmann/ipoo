import Locomotiva
import Vagao
import Trem
import Garagem

garagem_locomotivas = Garagem.Garagem(200)
garagem_vagoes = Garagem.Garagem(200)
garagem_trens = Garagem.Garagem(200)


def opcoes_menu():
    menu = '''
    MENU TREM
    1 - Adicionar Vagão
    2 - Adicionar Locomotiva
    3 - Adicionar Trem
    4 - Remover Vagao
    5 - Remover Locomotiva
    6 - Remover Trem
    7 - Engatar Vagão/Locomotiva no trem
    8 - Desengatar Vagão/Locomotiva
    9 - Esvaziar Garagem
    10 - Esvaziar Trem
    11 - Ver todos os vagões da garagem
    12 - Ver todos as locomotivas da garagem
    13 - Ver todos os trens da garagem
    14 - Ver todos os veiculos da garagem
    15 - Ver a quantidade de veiculos da garagem
    16 - Encerrar programa
    '''
    return menu


def init():
    locomotiva1 = Locomotiva.Locomotiva(100.0, 500.0)
    locomotiva2 = Locomotiva.Locomotiva(100.0, 500.0)
    garagem_locomotivas.estacionar(locomotiva1)
    garagem_locomotivas.estacionar(locomotiva2)

    vagao1 = Vagao.Vagao(200.0)
    vagao2 = Vagao.Vagao(500.0)
    vagao3 = Vagao.Vagao(100.0)
    garagem_vagoes.estacionar(vagao1)
    garagem_vagoes.estacionar(vagao2)
    garagem_vagoes.estacionar(vagao3)

    trem1 = Trem.Trem()
    garagem_trens.estacionar(trem1)


def menu():
    while True:
        print(opcoes_menu)
        opcao = int(input("Digite o numero correspondente a opção desejada: "))
        match opcao:
            case 1 | 2 | 3:
                cadastro(opcao)
            case 4 | 5 | 6:
                remocao(opcao)
            case 7:
                engatar_no_trem()
            case 8:
                desengatar()
            case 9:
                opcao = int(input("1 - Vagao, 2 - Locomotiva, 3 - Trem: "))
                if opcao == 1:
                    garagem_vagoes.esvaziar_garagem()
                elif opcao == 2:
                    garagem_locomotivas.esvaziar_garagem()
                else:
                    garagem_trens.esvaziar_garagem()
                print("Garagem esvaziada com sucesso!")
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                break
            case _:
                print("Opção inválida, tente novamente")


def cadastro(opcao):

    if opcao == 3:
        trem = Trem()
        cadastro = garagem_trens.estacionar(trem)
    else:
        peso = float(input("Digite o peso: "))
        if opcao == 1:
            vagao = Vagao.Vagao(peso)
            cadastro = garagem_vagoes.estacionar(vagao)
        else:
            combustivel = float(input("Digite a quantidade de combustivel: "))
            locomotiva = Locomotiva.Locomotiva(combustivel, peso)
            cadastro = garagem_locomotivas.estacionar(locomotiva)

    if cadastro:
        print("Cadastro realizado com sucesso")
    else:
        print("ERRO. Não foi possivel realizar cadastro")


def remocao(opcao):
    id = int(input("Digite id do veiculo: "))
    if opcao == 4:
        vagao = garagem_vagoes.get_veiculo_por_id(id)
        remocao = garagem_vagoes.remove_veiculo(vagao)
    elif opcao == 5:
        locomotiva = garagem_locomotivas.get_veiculo_por_id(id)
        remocao = garagem_locomotivas.remove_veiculo(locomotiva)
    else:
        trem = garagem_trens.get_veiculo_por_id(id)
        remocao = garagem_trens.remove_veiculo(trem)

    if remocao:
        print("Veiculo removido com sucesso")
    else:
        print("ERRO. Não foi possivel remover veiculo")


def engatar_no_trem():
    id = int(input("Digite id do trem"))
    trem = garagem_trens.get_veiculo_por_id(id)
    if trem is None:
        print(f"Não existe trem com o id: {id}")
        return
    opcao = input("(vagao) V ou L (Locomotiva)")
    if opcao == 'V':
        if trem.possui_locomotiva() == False:
            print("ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
            return
        else:
            id = int(input("Digite id do vagão: "))
            vagao = garagem_vagoes.get_veiculo_por_id(id)
            if vagao is None:
                print(f"Não existe vagao com o id: {id}")
                return
            trem.engatar(vagao)
            garagem_vagoes.remove_veiculo(vagao)
    else:
        id = int(input("Digite id da locomotiva: "))
        locomotiva = garagem_locomotivas.get_veiculo_por_id(id)
        if locomotiva is None:
            print(f"Não existe locomotiva com o id: {id}")
            return
        trem.engatar(locomotiva)
        garagem_locomotivas.remove_veiculo(locomotiva)


def desengatar():
    id = int(input("Digite id do trem"))
    trem = garagem_trens.get_veiculo_por_id(id)
    if trem is None:
        print(f"Não existe trem com o id: {id}")
        return
    opcao = input("(vagao) V ou L (Locomotiva)")
    if opcao == 'V':
        id = int(input("Digite id do vagão: "))
        vagao = garagem_vagoes.get_veiculo_por_id(id)
        if vagao is None:
            print(f"Não existe vagao com o id: {id}")
            return
        trem.desengatar(vagao)
        garagem_vagoes.estacionar(vagao)
    else:
        id = int(input("Digite id da locomotiva: "))
        locomotiva = garagem_locomotivas.get_veiculo_por_id(id)
        if locomotiva is None:
            print(f"Não existe locomotiva com o id: {id}")
            return
        trem.desengatar(locomotiva)
        garagem_locomotivas.estacionar(locomotiva)


# locomotiva1 = Locomotiva.Locomotiva(100.0, 500.0)
# locomotiva2 = Locomotiva.Locomotiva(100.0, 500.0)
# garagem_locomotivas.estacionar(locomotiva1)
# garagem_locomotivas.estacionar(locomotiva2)

# vagao1 = Vagao.Vagao(200.0)
# vagao2 = Vagao.Vagao(500.0)
# vagao3 = Vagao.Vagao(100.0)
# garagem_vagoes.estacionar(vagao1)
# garagem_vagoes.estacionar(vagao2)
# garagem_vagoes.estacionar(vagao3)


# trem1 = Trem.Trem()
# garagem_trens.estacionar(trem1)

# print(trem1)

# trem1.engatar(locomotiva1)
# trem1.engatar(vagao1)
# trem1.engatar(vagao2)
# trem1.engatar(vagao3)

# print(trem1)

# trem1.desengatar(vagao1)

# print(trem1)

print(menu())

# if type(parte_trem) == Locomotiva:
#     GaragemLocomotiva.estaciona_locomotiva(parte_trem)
# else:
#     GaragemVagao.estaciona_vagao(parte_trem)
