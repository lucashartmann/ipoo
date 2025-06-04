from Models import Estante
import View


class Construtor:

    estante = Estante()

    def cadastrar_livro(livro):
        cadastro = Construtor.estante.append(livro)
        if cadastro:
            View.View.imprimir("Livro cadastrado com sucesso!")
        else:
            View.View.imprimir("ERRO ao cadastrar livro")

    def remover_livro(titulo):
        livro = Construtor.estante.get_livro_por_titulo(titulo)
        if livro:
            remocao = Construtor.estante.remove(livro)
            if remocao:
                View.View.imprimir(livro, "removido com sucesso!")
            else:
                View.View.imprimir("ERRO ao remover livro")
        else:
            View.View.imprimir(
                f"ERRO. Não existe livro cadastrado com o titulo {titulo}")

    def ver_livros_cadastrados():
        livros_cadastrados = Construtor.estante.get_lista_livros()
        if livros_cadastrados:
            View.View.imprimir("LIVROS CADASTRADOS:")
            View.View.imprimir_lista(livros_cadastrados)
        else:
            View.View.imprimir("ERRO, lista vazia")
