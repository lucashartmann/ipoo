class Jogador:
    def __init__(self):
        self.vida = 10
        self.mana = 10

    def get_vida(self):
        return self.vida

    def get_mana(self):
        return self.vida

    def atacar(self, inimigo, item):
        dano = item.get_dano()
        vida_restante_inimigo = item.get_dano() - inimigo.get_vida()
        inimigo.set_vida(vida_restante_inimigo)
        self.mana = self.mana - (item.get_dano() * 0.2)
        return (dano, vida_restante_inimigo)
