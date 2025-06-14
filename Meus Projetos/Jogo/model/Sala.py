class Sala:

    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None
        self.baixo = None
        self.cima = None

    def get_nome(self):
        return self.nome

    def get_esquerda(self):
        return self.esquerda

    def get_direita(self):
        return self.direita

    def get_baixo(self):
        return self.baixo

    def get_cima(self):
        return self.cima

    def set_esquerda(self, sala):
        self.esquerda = sala

    def set_direita(self, sala):
        self.direita = sala

    def set_cima(self, sala):
        self.cima = sala

    def set_baixo(self, sala):
        self.baixo = sala

    def __str__(self):
        return f"Sala [Nome: {self.get_nome()}, esquerda = {self.get_esquerda()}, direita = {self.get_direita()}, baixo = {self.get_baixo()}, cima = {self.get_cima()}]"
