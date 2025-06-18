def mostrar_mensagem(string):
    print(string)

def mostrar_itens_lista(lista):
    for item in lista:
        mostrar_mensagem(item)

def pegar_dado(mensagem):
    dado = input(f"mensagem: ")
    return dado