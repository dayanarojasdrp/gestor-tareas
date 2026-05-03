import tempfile
import unittest
from pathlib import Path

from task_manager.manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_manager_adds_task(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = TaskManager(storage_path=Path(temp_dir) / "tasks.json")

            task = manager.add_task("Study Python")

            self.assertEqual(task.id, 1)
            self.assertEqual(task.title, "Study Python")
            self.assertEqual(manager.tasks, [task])

    def test_manager_completes_task(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = TaskManager(storage_path=Path(temp_dir) / "tasks.json")
            manager.add_task("Study Python")

            completed = manager.complete_task(0)

            self.assertTrue(completed)
            self.assertTrue(manager.tasks[0].completed)


if __name__ == "__main__":
    unittest.main()
