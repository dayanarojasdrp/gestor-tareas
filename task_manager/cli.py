from task_manager.manager import TaskManager


def menu():
    manager = TaskManager()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Salir")

        option = input("Elige una opción: ")

        if option == "1":
            title = input("Título de la tarea: ")
            manager.add_task(title)
        elif option == "2":
            manager.list_tasks()
        elif option == "3":
            try:
                index = int(input("Número de tarea a completar: ")) - 1
                manager.complete_task(index)
            except ValueError:
                print("Debes ingresar un número válido.")
        elif option == "4":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción inválida")
