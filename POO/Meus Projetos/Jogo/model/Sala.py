class Sala:

    def __init__(self, nome):
        self.nome = nome

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
        str = f"Sala [Nome: {self.get_nome()}"
        if self.get_baixo():
            str += f", baixo = {self.get_baixo()}"
        if self.get_cima():
            str += f", cima = {self.get_cima()}"
        if self.get_direita():
            str += f", direita = {self.get_direita()}"
        if self.get_esquerda():
            str += f", esquerda = {self.get_esquerda()}"
        str += "]"
        return str
