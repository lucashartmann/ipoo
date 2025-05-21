import AgendaModel
import AgendaView


def ctrl_listar():
    registros = AgendaModel.listagem(AgendaModel.minha_agenda)
    if registros:
        AgendaView.imprimir(registros)
    else:
        print("Erro")


def ctrl_ajuda():
    AgendaView.imprimir_ajuda()


def test_ctrl_cadastrar():
    email = 'srz@email.com'
    nome = 'Sr. Z'
    idade = 32
    endereco = 'Rua z'
    cadastrar = AgendaModel.cadastrar(
        AgendaModel.minha_agenda, email, nome, idade, endereco)
    if cadastrar:
        print(f'{email} cadastrado com sucesso')
    else:
        print(f'Não cadastrado: {email} já existe na agenda')


def test_ctrl_apagar():
    sucesso = AgendaModel.apagar(AgendaModel.minha_agenda, 'sry@email.com')
    if sucesso:
        print("Registro excluído")
    else:
        print("Registro inexistente")


def test_ctrl_atualizar():
    email = 'srz@email.com'
    nome = 'Senhor Ze'
    idade = 31
    endereco = 'Rua do sr. Z'
    atualizar = AgendaModel.atualizar(
        AgendaModel.minha_agenda, email, nome, idade, endereco)
    if atualizar:
        print(f'{email} atualizado com sucesso')
        dados = AgendaModel.consultar(AgendaModel.minha_agenda, email)
        AgendaView.imprimir_um((email, dados))
    else:
        print(f'{email} não existe na agenda')


def test_ctrl_favoritar():
    test_ctrl_cadastrar()
    print(f'*** Favoritando...')
    email = "srz@email.com"
    favoritar = AgendaModel.favoritar(
        AgendaModel.minha_agenda)
    if favoritar:
        print(f'{email} favoritado!')
    else:
        print(f"{email} inexistente")
