from gestor import GestorTareas

def menu():
    gestor = GestorTareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Título de la tarea: ")
            gestor.agregar_tarea(nombre)
        elif opcion == "2":
            gestor.listar_tareas()
        elif opcion == "3":
            try:
                indice = int(input("Número de tarea a completar: ")) - 1
                gestor.completar_tarea(indice)
            except ValueError:
                print("Debes ingresar un número válido.")
        elif opcion == "4":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
