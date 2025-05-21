import AgendaModel
import AgendaController

import sys

AgendaModel.agenda_init()
print("Agenda 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1]  # python AgendaApp.py listar
except IndexError:
    print("ERRO")
    AgendaController.ctrl_ajuda()
    sys.exit(0)

if comando == "listar":
    AgendaController.ctrl_listar()
if comando == "ajuda":
    AgendaController.ctrl_ajuda()
