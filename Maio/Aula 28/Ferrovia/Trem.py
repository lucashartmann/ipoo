import Vagao
import Locomotiva


class Trem:

    def __init__(self, locomotivas, vagoes):
        # self.capacidade = capacidade
        self.quant_passageiros = 0
        self.locomotivas = locomotivas
        self.vagoes = vagoes
        # self.quant_vagoes = 0
        # self.quant_locomotivas = 0
        # self.quant_max_vagoes_suportados = 0
        # self.quant_max_locomotivas_suportados = 0
        self.peso_suportado = 200000.00
        self.peso_atual = 0
        self.trem = [locomotivas, vagoes]

    def get_locomotiva(self):
        return self.locomotiva

    def get_vagoes(self):
        return self.vagoes

    def get_peso_suportado(self):
        return self.peso_suportado

    def get_peso_atual(self):
        return self.peso_atual

    def engatar(self, parte_trem):
        if (type(parte_trem) == Locomotiva.Locomotiva or type(parte_trem) == Vagao.Vagao) and parte_trem not in self.trem:
            self.peso_atual += parte_trem.get_peso()
            self.trem.append(parte_trem)
            return True
        return False

    def desengatar(self, parte_trem):
        if (type(parte_trem) == Locomotiva.Locomotiva or type(parte_trem) == Vagao.Vagao) and parte_trem in self.trem:
            ultimo_index = len(self.trem) - 1
            index_parte_trem = self.trem.index(parte_trem)
            if index_parte_trem == ultimo_index:
                self.trem.remove(parte_trem)
                return True
        return False

    def get_trem(self):
        return self.trem

    def __str__(self):
        string_parte_trem = " <- ".join(str(parte_trem)
                                        for parte_trem in self.get_trem())
        return f"Trem: [{string_parte_trem}] "
