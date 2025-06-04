class Estante:
    def __init__(self):
        self.livros_comprados = []

    def adicionar_livro(self, livro):
        if livro not in self.livros_comprados:
            self.livros_comprados.append(livro)
            return True
        return False
    
    def remover_livro(self, livro):
        if livro in self.livros_comprados:
            self.livros_comprados.remove(livro)
            return True
        return False
    
    def get_lista_livros(self):
        return self.livros_comprados
    
    def get_lista_livros_nao_iniciados(self):
        livros_finalizados = []
        for livro in self.livros_comprados:
            if livro.get_status() == "Leitura não iniciada":
                livros_finalizados.append(livro)
        return livros_finalizados
    
    def get_lista_livros_em_curso(self):
        livros_em_curso = []
        for livro in self.livros_comprados:
            if livro.get_status() == "Leitura em curso":
                livros_em_curso.append(livro)
        return livros_em_curso
    
    def get_lista_livros_finalizados(self):
        livros_finalizados = []
        for livro in self.livros_comprados:
            if livro.get_status() == "Leitura encerrada":
                livros_finalizados.append(livro)
        return livros_finalizados
    
    def get_livro_por_titulo(self, titulo):
        for livro in self.livros_comprados:
            if livro.get_titulo() == titulo:
                return livro
        return None