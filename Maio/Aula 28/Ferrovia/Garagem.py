class Garagem:

    def __init__(self, capacidade):
        self.veiculos_ferroviarios = []
        self.capacidade = capacidade
        self.quant_veiculos_ferroviarios = 0

    def estacionar(self, veiculo):
        if veiculo not in self.veiculos_ferroviarios and self.capacidade >= self.quant_veiculos_ferroviarios:
            self.veiculos_ferroviarios.append(veiculo)
            self.quant_veiculos_ferroviarios += 1
            return True
        return False

    def remove_veiculo(self, veiculo):
        if veiculo in self.veiculos_ferroviarios:
            self.veiculos_ferroviarios.remove(veiculo)
            return True
        return False

    def get_veiculos_ferroviarios(self):
        return self.veiculos_ferroviarios

    def get_capacidade(self):
        return self.capacidade

    def get_quant_veiculos_ferroviarios(self):
        return self.get_quant_veiculos_ferroviarios

    def get_veiculo_por_id(self, id):
        for veiculo in self.get_veiculos_ferroviarios:
            if veiculo.get_id() == id:
                return veiculo
        return None
    
    def esvaziar_garagem(self):
        self.veiculos_ferroviarios.clear()
