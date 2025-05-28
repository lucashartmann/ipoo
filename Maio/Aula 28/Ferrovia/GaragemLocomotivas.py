class GaragemLocomotivas:

    def __init__(self, capacidade):
        self.locomotivas_estacionadas = []
        self.capacidade = capacidade
        self.quant_locomotivas_estacionadas = 0

    def estaciona_locomotiva(self, locomotiva):
        if locomotiva not in self.locomotivas_estacionadas and self.capacidade >= self.quant_locomotivas_estacionadas:
            self.locomotivas_estacionadas.append(locomotiva)
            self.quant_locomotivas_estacionadas += 1
            return True
        return False

    def remove_locomotiva(self, locomotiva):
        if locomotiva in self.locomotivas_estacionadas:
            self.locomotivas_estacionadas.remove(locomotiva)
            return True
        return False

    def get_locomotivas_estacionadas(self):
        return self.locomotivas_estacionadas

    def get_capacidade(self):
        return self.capacidade

    def get_quant_locomotivas_estacionadas(self):
        return self.get_quant_locomotivas_estacionadas
