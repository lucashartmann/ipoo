from models import Locomotiva, Vagao, Trem


class Trem:
    id = 0

    def __init__(self):
        self.id = self.gerar_id()
        # self.capacidade = capacidade
        # self.quant_passageiros = 0
        # self.quant_vagoes = 0
        # self.quant_locomotivas = 0
        # self.quant_max_vagoes_suportados = 0
        # self.quant_max_locomotivas_suportados = 0
        self.peso_suportado = 200000.00
        self.peso_atual = 0
        self.trem = []

    def gerar_id(self):
        Trem.id += 1
        return Trem.id

    def get_id(self):
        return self.id

    def get_locomotiva(self):
        return self.locomotiva

    def get_vagoes(self):
        return self.vagoes

    def get_peso_suportado(self):
        return self.peso_suportado

    def get_peso_atual(self):
        return self.peso_atual

    def engatar(self, veiculo):
        if (type(veiculo) == Locomotiva.Locomotiva or type(veiculo) == Vagao.Vagao) and veiculo not in self.trem and self.peso_atual <= self.peso_suportado:
            self.peso_atual += veiculo.get_peso()
            self.trem.append(veiculo)
            return True
        return False

    def desengatar(self, veiculo):
        if (type(veiculo) == Locomotiva.Locomotiva or type(veiculo) == Vagao.Vagao) and veiculo in self.trem and self.peso_atual <= self.peso_suportado:
            ultimo_index = len(self.trem) - 1
            index_veiculo = self.trem.index(veiculo)
            if index_veiculo == ultimo_index:
                self.trem.remove(veiculo)
                self.peso_atual -= veiculo.get_peso()
                return True
            else:
                for veiculo_ferroviario in self.trem[index_veiculo::]:
                    self.trem.remove(veiculo_ferroviario)
                    # self.peso_atual -= veiculo.get_peso() ?
                    self.peso_atual -= veiculo_ferroviario.get_peso()
                return True
        return False

    def get_trem(self):
        return self.trem

    def esvaziar(self):
        self.trem.clear()

    def __str__(self):
        string_veiculo = " <- ".join(str(veiculo)
                                     for veiculo in self.get_trem())
        return f"Trem: [{string_veiculo}] "
