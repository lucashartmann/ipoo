from model import Mochila
from model import Item
from model import Bau
from model import Sala

mochila1 = Mochila.Mochila()
item1 = Item.Item()
item2 = Item.Item()
bau1 = Bau.Bau()

sala1 = Sala.Sala("Sala Inicial")
sala2 = Sala.Sala("Sala de Baús")

sala1.set_direita(sala2)

print(item1)
print(item2)
