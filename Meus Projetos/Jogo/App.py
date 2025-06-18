from model import Mochila
from model import Item
from model import Bau
from model import Sala
import View
import Controller
import sys

Controller.init()
Controller.carregar_bau()

comando = sys.argv[1::]

# python App.py ver_bau
 
match comando:
    case["ver_bau"]:
        Controller.ver_bau()
    case ["pegar_item_bau", item, quant]:
        Controller.pegar_item_bau(item, quant)

Controller.salvar_bau()
    


