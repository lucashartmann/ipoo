from models import Locomotiva, Vagao, Trem, Garagem


class ControllerCMD:

    def ajuda():
        comandos = '''
Comandos para a execução do programa:

1. "adicionar_vagao peso"
2. "adiconar_locomotiva combustivel peso"
3. "adicionar_trem"
4. "remover id_trem id_veiculo"
5. "engatar id_trem id_veiculo" 
6. "desengatar id_trem id_veiculo"
7. "esvaziar_garagem_locomotiva" 
8. "esvaziar_garagem_vagao"
9. "esvaziar_garagem_trem"
10. "esvaziar_trem id_veiculo"
11. "ajuda"
        '''
        return comandos

    def adicionar_vagao(garagem, peso):
        vagao = Vagao.Vagao(peso)
        cadastro = garagem.estacionar(vagao)
        if cadastro:
            print("Cadastro realizado com sucesso")
            print(vagao)
        else:
            print("ERRO. Não foi possivel realizar cadastro")

    def adicionar_locomotiva(garagem, combustivel, peso):
        locomotiva = Locomotiva.Locomotiva(combustivel, peso)
        cadastro = garagem.estacionar(locomotiva)
        if cadastro:
            print("Cadastro realizado com sucesso")
            print(locomotiva)
        else:
            print("ERRO. Não foi possivel realizar cadastro")

    def adicionar_trem(garagem):
        trem = Trem()
        cadastro = garagem.estacionar(trem)
        if cadastro:
            print("Cadastro realizado com sucesso")
            print(trem)
        else:
            print("ERRO. Não foi possivel realizar cadastro")

    def remover(garagem, id):
        veiculo = garagem.get_veiculo_por_id(id)
        remocao = garagem.remove_veiculo(veiculo)
        if remocao:
            print(veiculo, "removido com sucesso")
        else:
            print("ERRO. Não foi possivel remover", veiculo)

    def engatar(garagem, id_trem, id_veiculo):
        trem = garagem.get_veiculo_por_id(id_trem)
        if trem is None:
            print(f"Não existe trem com o id: {id_trem}")
            return
        else:
            veiculo = garagem.get_veiculo_por_id(id_veiculo)
            if type(veiculo) == Vagao.Vagao:
                if trem.possui_locomotiva() == False:
                    print(
                        "ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
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

    def desengatar(garagem, id_trem, id_veiculo):
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

    def remover_trens_da_garagem(garagem):
        garagem.remover_todos_trens()
        print("Trens removidos com sucesso")
        print("TRENS NA GARAGEM:")
        print(garagem.get_lista_trens())

    def remover_locomotivas_da_garagem(garagem):
        garagem.remover_todas_locomotivas()
        print("Locomotivas removidas com sucesso")
        print("LOCOMOTIVAS NA GARAGEM:")
        print(garagem.get_lista_locomotivas())

    def remover_vagoes_da_garagem(garagem):
        garagem.remover_todos_vagoes()
        print("Vagões removidos com sucesso")
        print("VAGÕES NA GARAGEM:")
        print(garagem.get_lista_vagoes())

    def esvaziar_trem(garagem, id):
        trem = garagem.get_veiculo_por_id(id)
        if trem is None:
            print(f"Não existe trem com o id: {id}")
            return
        trem.esvaziar()
        print("Trem esvaziado com sucesso!", trem)
