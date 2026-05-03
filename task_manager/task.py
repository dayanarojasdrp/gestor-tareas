from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    @property
    def nombre(self):
        return self.title

    @property
    def completada(self):
        return self.completed

    def complete(self):
        self.completed = True

    def completadam(self):
        self.complete()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False),
        )

    def __str__(self):
        status = "Completada" if self.completed else "No Completada"
        return f"{self.title} - {status}"


Tarea = Task
