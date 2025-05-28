class GaragemVagoes:

    def __init__(self, capacidade):
        self.vagoes_estacionados = []
        self.capacidade = capacidade
        self.quant_vagoes_estacionados = 0

    def estaciona_vagao(self, vagao):
        if vagao not in self.vagoes_estacionados and self.capacidade >= self.quant_vagoes_estacionados:
            self.vagoes_estacionados.append(vagao)
            self.quant_vagoes_estacionados += 1
            return True
        return False

    def remove_vagao(self, vagao):
        if vagao in self.vagoes_estacionados:
            self.vagoes_estacionados.remove(vagao)
            return True
        return False

    def get_capacidade(self):
        return self.capacidade

    def get_quant_vagoes_estacionados(self):
        return self.quant_vagoes_estacionados

    def get_vagoes_estacionados(self):
        return self.vagoes_estacionados
