# Model da Agenda

agenda = {}


def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    if email not in agenda.keys():
        agenda[email] = [nome, idade, endereco, favorito]
        return True
    return False


def atualizar(agenda, email, nome, idade, endereco, favorito=False):
    try:
        agenda[email] == [nome, idade, endereco, favorito]
        return agenda[email] 
    except KeyError:
        return None


def get_registro_por_email(agenda, email):
    try:
        return agenda[email]
    except KeyError:
        return None


def get_todos_registros(agenda):
    return agenda.items()


def apagar(agenda, email):
    try:
        del agenda[email]
        return True
    except KeyError:
        return False


def favoritar(agenda, email):
    try:
        agenda[email][3] = True
        return True
    except KeyError:
        return False


def agenda_init():
    cadastrar(agenda, "lucas@dfsdfdfd", 'Lucas', 21, "São Manuel")
    cadastrar(agenda, "fernando@dfdfd", 'Pedro', 61, "São Manuel")

# View da Agenda


def imprimir_todos_registros(registros):
    for email, dados in registros:
        print(f'''Email: {email}
    Nome: {dados[0]}
    Endereco: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}
    ''')


def imprimir_registro(email, dados):
    print(f'''Email: {email}
    Nome: {dados[0]}
    Endereco: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}
    ''')

# Controlador da Agenda


print("### Agenda 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS ###")

# agenda_init()

email = "marcelo@hotmail.com"
nome = "Marcelo"
idade =  87
endereco = "São Fernandes 88" 

cadastro = cadastrar(agenda, email, nome, idade, endereco)

if cadastro:
    print("Sucesso!", email, "cadastrado")
else:
    print("Erro")

atualizacao = atualizar(agenda, email, 'João', 90, "São Pitanguinhas")

if atualizacao:
    print("Sucesso!", email, "atualizado")
else:
    print("Erro")


todos_registros = get_todos_registros(agenda)
imprimir_todos_registros(todos_registros)

registro = get_registro_por_email(agenda, email)

if registro:
    imprimir_registro(email, registro)
else:
    print("Registro não eccontrado")

sucesso = apagar(agenda, "fernando@dfdfd")

if sucesso:
    print("Sucesso")
else:
    print("ERRO")

favorito = favoritar(agenda, email)

#Continuar