from models import Locomotiva, Vagao, Trem, Garagem


garagem = Garagem.Garagem(900)


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
    garagem.estacionar(locomotiva1)
    garagem.estacionar(locomotiva2)

    vagao1 = Vagao.Vagao(200.0)
    vagao2 = Vagao.Vagao(500.0)
    vagao3 = Vagao.Vagao(100.0)
    garagem.estacionar(vagao1)
    garagem.estacionar(vagao2)
    garagem.estacionar(vagao3)

    trem1 = Trem.Trem()
    garagem.estacionar(trem1)


def menu():
    while True:
        print(opcoes_menu())
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
                    garagem.remover_todos_vagoes()
                    print("Vagões removidos com sucesso")
                    print("VAGÕES NA GARAGEM:")
                    print(garagem.get_lista_vagoes())
                elif opcao == 2:
                    garagem.remover_todas_locomotivas()
                    print("Locomotivas removidas com sucesso")
                    print("LOCOMOTIVAS NA GARAGEM:")
                    print(garagem.get_lista_locomotivas())
                else:
                    garagem.remover_todos_trens()
                    print("Trens removidos com sucesso")
                    print("TRENS NA GARAGEM:")
                    print(garagem.get_lista_trens())
            case 10:
                id = int(input("Digite o id do trem: "))
                trem = garagem.get_veiculo_por_id(id)
                if trem is None:
                    print(f"Não existe trem com o id: {id}")
                    return
                trem.esvaziar()
                print("Trem esvaziado com sucesso!")
                print(trem)
            case 11:
                vagoes = garagem.get_lista_vagoes()
                if not vagoes:
                    print("Não há vagões na garagem")
                else:
                    print("VAGÕES NA GARAGEM:")
                    for vagao in vagoes:
                        print(vagao)
            case 12:
                Locomotivas = garagem.get_lista_locomotivas()
                if not Locomotivas:
                    print("Não há locomotivas na garagem")
                else:
                    print("LOCOMOTIVAS NA GARAGEM:")
                    for locomotiva in Locomotivas:
                        print(locomotiva)
            case 13:
                trens = garagem.get_lista_trens()
                if not trens:
                    print("Não há trens na garagem")
                else:
                    print("TRENS NA GARAGEM:")
                    for trem in trens:
                        print(trem)
            case 14:
                veiculos = garagem.get_veiculos_ferroviarios()
                if not veiculos:
                    print("Não há veículos na garagem")
                else:
                    print("VEÍCULOS NA GARAGEM:")
                    for veiculo in veiculos:
                        print(veiculo)
            case 15:
                print(
                    f"Quantidade de veículos na garagem: {garagem.get_quant_veiculos_ferroviarios()}")
            case 16:
                break
            case _:
                print("Opção inválida, tente novamente")


def cadastro(opcao):

    if opcao == 3:
        trem = Trem.Trem()
        cadastro = garagem.estacionar(trem)
    else:
        peso = float(input("Digite o peso: "))
        if opcao == 1:
            vagao = Vagao.Vagao(peso)
            cadastro = garagem.estacionar(vagao)
        else:
            combustivel = float(input("Digite a quantidade de combustivel: "))
            locomotiva = Locomotiva.Locomotiva(combustivel, peso)
            cadastro = garagem.estacionar(locomotiva)

    if cadastro:
        print("Cadastro realizado com sucesso")
    else:
        print("ERRO. Não foi possivel realizar cadastro")


def remocao(opcao):
    id = int(input("Digite id do veiculo: "))
    if opcao == 4:
        vagao = garagem.get_veiculo_por_id(id)
        remocao = garagem.remove_veiculo(vagao)
    elif opcao == 5:
        locomotiva = garagem.get_veiculo_por_id(id)
        remocao = garagem.remove_veiculo(locomotiva)
    else:
        trem = garagem.get_veiculo_por_id(id)
        remocao = garagem.remove_veiculo(trem)

    if remocao:
        print("Veiculo removido com sucesso")
    else:
        print("ERRO. Não foi possivel remover veiculo")


def engatar_no_trem():
    id = int(input("Digite id do trem: "))
    trem = garagem.get_veiculo_por_id(id)
    if trem is None:
        print(f"Não existe trem com o id: {id}")
        return
    id = int(input("Digite id do veiculo: "))
    veiculo = garagem.get_veiculo_por_id(id)
    if type(veiculo) == Vagao.Vagao:
        if trem.possui_locomotiva() == False:
            print("ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
            return
    if veiculo is None:
        print(f"Não existe veiculo com o id: {id}")
        return
    trem.engatar(veiculo)
    garagem.remove_veiculo(veiculo)


def desengatar():
    id = int(input("Digite id do trem: "))
    trem = garagem.get_veiculo_por_id(id)
    if trem is None:
        print(f"Não existe trem com o id: {id}")
        return
    id = int(input("Digite id do veiculo: "))
    veiculo = garagem.get_veiculo_por_id(id)
    if veiculo is None:
        print(f"Não existe veiculo com o id: {id}")
        return
    trem.desengatar(veiculo)
    garagem.estacionar(veiculo)


if __name__ == "__main__":
    init()
    menu()
