import random

objeto = ["Rocha", "Espada", "Capa", "Foice", "Capacete", "Peitoral", "Calça", "Picareta", "Machado", "Cenoura", "Gema", "Moeda"]
adjetivo = ["Feroz", "Fulminante", "Vingativa", "Bela como a Lua", "Reluzente", "Fervescente"]
complemento = ["Forjada na lua", "do Minotauro", "dos confins do inferno", "Enferrujada", "Perfeita", "Usada pelo Rei de Minas"]

def gerar_numero(lenght):
    numero = int(random.randrange(lenght))
    return numero

def gerar_nome():
    nome = f"{objeto[gerar_numero(len(objeto))]} {adjetivo[gerar_numero(len(adjetivo))]} {complemento[gerar_numero(len(complemento))]}"    
    return nome

item1 = gerar_nome()
item2 = gerar_nome()
item3 = gerar_nome()

print("Item:", item1)
print("Item:", item2)
print("Item:", item3)