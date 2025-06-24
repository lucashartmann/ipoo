from models.Cena import Cena
from models.Personagem import Mago
from models.Personagem import Guerreiro
from models.Personagem import Personagem
from models.Item import Item

hall = Cena("Hall")
sala = Cena("Sala")
calabouco1 = Cena("Calabouço 1")
cela1 = Cena("Cela 1")
calabouco2 = Cena("Calabouço 2")
cela2 = Cena("Cela 2")
patio = Cena("Patio")
heroi = Mago()

heroi.sala = hall

hall.leste = sala
sala.sul = calabouco1
sala.oeste = hall
calabouco1.leste = cela1
calabouco1.norte = sala
calabouco1.sul = calabouco2
cela1.oeste = calabouco1
cela1.sul = cela2
calabouco2.norte = calabouco1
calabouco2.leste = cela2
cela2.norte = cela1
cela2.oeste = calabouco2
cela2.leste = patio
patio.oeste = cela2


# heroi.andar_leste()
# heroi.andar_sul()
# heroi.andar_leste()
# heroi.andar_oeste()
# heroi.andar_sul()

# heroi.coletar("espada")
# heroi.coletar("lança")
# heroi.equipar("espada")
# heroi.atacar()
# heroi.equipar("lança")
# heroi.atacar()
# heroi.soltar("espada")

# heroi.andar_leste()
# heroi.andar_leste()
# heroi.andar_oeste()
# heroi.andar_oeste()

# #subindo agora...
# heroi.andar_norte()
# heroi.andar_norte()
# heroi.andar_oeste()

item1 = Item()
hall.colocar_item(item1, "espada")
heroi.coletar_item("espada")
heroi.equipar_item("espada")
heroi.atacar()
