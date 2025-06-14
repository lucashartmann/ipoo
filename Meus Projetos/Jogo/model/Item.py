import random


class Item:

    def __init__(self):
        self.dano = 0
        self.quant = 0
        self.protecao = 0
        self.nome = self.gerar_nome()

    def gerar_nome(self):
        objetos = [
            {"nome": "Rocha", "genero": "f"},
            {"nome": "Espada", "genero": "f", "dano": 5},
            {"nome": "Capa", "genero": "f"},
            {"nome": "Foice", "genero": "f", "dano": 2},
            {"nome": "Capacete", "genero": "m", "protecao": 5},
            {"nome": "Peitoral", "genero": "m", "protecao": 5},
            {"nome": "Calça", "genero": "f", "protecao": 5},
            {"nome": "Picareta", "genero": "f", "dano": 2},
            {"nome": "Machado", "genero": "m", "dano": 2},
            {"nome": "Cenoura", "genero": "f", "dano": 2},
            {"nome": "Gema", "genero": "f"},
            {"nome": "Moeda", "genero": "f"}
        ]

        adjetivos = [
            {"f": "Feroz", "m": "Feroz"},
            {"f": "Fulminante", "m": "Fulminante", "dano": 5},
            {"f": "Vingativa", "m": "Vingativo", "dano": 5},
            {"f": "Bela como a Lua", "m": "Belo como a Lua"},
            {"f": "Reluzente", "m": "Reluzente"},
            {"f": "Fervescente", "m": "Fervescente"}
        ]

        complementos = [
            {"f": "Forjada na lua", "m": "Forjado na lua", "dano": 5, "protecao": 5},
            {"f": "do Minotauro", "m": "do Minotauro", "dano": 5, "protecao": 5},
            {"f": "dos confins do inferno", "m": "dos confins do inferno"},
            {"f": "Enferrujada", "m": "Enferrujado"},
            {"f": "Perfeita", "m": "Perfeito"},
            {"f": "Usada pelo Rei de Minas", "m": "Usado pelo Rei de Minas"}
        ]

        objeto = random.choice(objetos)
        adjetivo = random.choice(adjetivos)
        complemento = random.choice(complementos)

        try:
            if "dano" in objeto.keys():
                self.set_dano(int(objeto["dano"]))
                if "dano" in adjetivo.keys():
                    dano = self.get_dano() + adjetivo["dano"]
                    self.set_dano(dano)
                if "dano" in complemento.keys():
                    dano = self.get_dano() + complemento["dano"]
                    self.set_dano(dano)
                if complemento["f"] == "Enferrujada" or complemento["m"] == "Enferrujado":
                    self.dano -= 2
            if "protecao" in objeto.keys():
                self.protecao = objeto["protecao"]
                if "protecao" in adjetivo.keys():
                    self.protecao += adjetivo["protecao"]
                if "protecao" in complemento.keys():
                    self.protecao += complemento["protecao"]
                if complemento["f"] == "Enferrujada" or complemento["m"] == "Enferrujado":
                    self.protecao -= 1
        except KeyError:
            pass
        genero_objeto = objeto["genero"]

        nome = f"{objeto["nome"]} {adjetivo[genero_objeto]} {complemento[genero_objeto]}"

        return nome

    def get_nome(self):
        return self.nome

    def get_quant(self):
        return self.quant

    def set_quant(self, quantidade):
        self.quant = quantidade

    def set_dano(self, novo_Dano):
        self.dano = novo_Dano

    def get_dano(self):
        return self.dano

    def __str__(self):
        if self.dano > 0:
                    return f"Item [Nome: {self.get_nome()}, quantidade = {self.get_quant()}, dano = {self.get_dano()}]"

        if self.protecao > 0:
                    return f"Item [Nome: {self.get_nome()}, quantidade = {self.get_quant()}, protecao = {self.protecao}]"

        if self.dano > 0 and self.protecao > 0:
                     return f"Item [Nome: {self.get_nome()}, quantidade = {self.get_quant()}, dano = {self.get_dano()}, protecao = {self.protecao}]"

        return f"Item [Nome: {self.get_nome()}, quantidade = {self.get_quant()}]"
