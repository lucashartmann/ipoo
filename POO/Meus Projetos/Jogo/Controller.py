import View
from model import Mochila
from model import Item
from model import Bau
from model import Sala
import shelve

bau1 = Bau.Bau()
mochila1 = Mochila.Mochila()
bau_db = shelve.open("bau.db",writeback=True)

def salvar_bau():
    bau_db["bau"] = bau1.get_itens_no_bau() 
    bau_db.close()

def carregar_bau():
    bau1.itens_no_bau = bau_db["bau"]
    
def ver_bau():
    View.mostrar_mensagem(bau1)

def init():
    item1 = Item.Item()
    item2 = Item.Item()

    sala1 = Sala.Sala("Sala Inicial")
    sala2 = Sala.Sala("Sala de Baús")
    sala3 = Sala.Sala("Spawn de Inimigos")

    sala1.set_direita(sala2)
    sala2.set_baixo(sala3)

    salvar_bau() # inicializar baú

def pegar_item_bau():
    View.mostrar_mensagem(bau1)
    nome = View.pegar_dado("Digite o nome do item")
    quant = int(View.pegar_dado("Digite a quant do item"))
    item_do_bau = bau1.get_item(nome, quant)
    if item_do_bau:
        mochila1.guardar(item_do_bau)
        View.mostrar_mensagem(mochila1)
    else:
        View.mostrar_mensagem("Erro ao pegar o item do baú")