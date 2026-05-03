import json
from pathlib import Path

from task_manager.task import Task


TASKS_FILE = Path("tareas.json")


def load_tasks(file_path=TASKS_FILE):
    path = Path(file_path)
    if not path.exists() or path.stat().st_size == 0:
        return []

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [Task.from_dict(item) for item in data]


def save_tasks(tasks, file_path=TASKS_FILE):
    path = Path(file_path)
    data = [task.to_dict() for task in tasks]

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
