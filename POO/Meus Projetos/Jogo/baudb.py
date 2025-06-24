import shelve
from model import Bau
from model import Sala

# '''
# um_bau = Bau.Bau()

# bau_db = shelve.open("bau.db",writeback=True)

# bau_db["bau"] = um_bau
# bau_db.close()


# '''
# bau_db = shelve.open("bau.db",writeback=True)
# um_bau = bau_db["bau"]
# print(um_bau)

sala1 = Sala.Sala("Sala Inicial")
sala2 = Sala.Sala("Sala de Baús")
sala3 = Sala.Sala("Spawn de Inimigos")

sala1.set_direita(sala2)
sala2.set_baixo(sala3)

print(sala1)