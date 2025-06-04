class View:

    def imprimir_lista(lista):
        for objeto in lista:
            print(objeto)

    def imprimir(mensagem):
        print(mensagem)

    def pedir_dado(mensagem):
        dado = input(f"{mensagem}: ")
        return dado