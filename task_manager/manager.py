from task_manager.storage import load_tasks, save_tasks
from task_manager.task import Task


class TaskManager:
    def __init__(self, storage_path=None):
        self.storage_path = storage_path
        self.tasks = load_tasks(storage_path) if storage_path else load_tasks()

    def add_task(self, title):
        task = Task(self._next_id(), title)
        self.tasks.append(task)
        self._save()
        return task

    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas")
            return

        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            self._save()
            return True

        print("Índice inválido")
        return False

    def agregar_tarea(self, nombre):
        return self.add_task(nombre)

    def listar_tareas(self):
        self.list_tasks()

    def completar_tarea(self, indice):
        return self.complete_task(indice)

    def _next_id(self):
        if not self.tasks:
            return 1

        return max(task.id for task in self.tasks) + 1

    def _save(self):
        if self.storage_path:
            save_tasks(self.tasks, self.storage_path)
        else:
            save_tasks(self.tasks)


GestorTareas = TaskManager
