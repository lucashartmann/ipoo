class Vagao:
    id = 0

    def __init__(self, peso):
        self.id = self.gerar_id()
        self.peso = peso

    def gerar_id(self):
        Vagao.id += 1
        return Vagao.id

    def get_peso(self):
        try:
            return self.peso
        except AttributeError:
            return 0

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            return 0

    def __str__(self):
        return f"Vagao [id = {self.get_id()}, peso = {self.get_peso()}]"
