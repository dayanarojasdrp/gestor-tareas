import unittest

from task_manager.task import Task


class TestTask(unittest.TestCase):
    def test_task_can_be_completed(self):
        task = Task(id=1, title="Study Python")

        task.complete()

        self.assertTrue(task.completed)

    def test_task_serializes_to_dict(self):
        task = Task(id=1, title="Study Python", completed=False)

        self.assertEqual(
            task.to_dict(),
            {
                "id": 1,
                "title": "Study Python",
                "completed": False,
            },
        )


if __name__ == "__main__":
    unittest.main()
