# gestor.py
from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre):
        self.tareas.append(Tarea(nombre))

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completadam()
        else:
            print("Índice inválido")
