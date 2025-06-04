class Leitura:
    def __init__(self, livro, pagina):
        self.pagina_atual = 0
        self.paginas_restantes = 0
        self.percentual_leitura = 0 

    def atualizar_leitura(self, pagina):
        self.pagina_atual += 1