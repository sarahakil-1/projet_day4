import unittest
import os
import json
from task_manager.core import add_task, delete_task, load_tasks, save_tasks
from task_manager.config import get_tasks_file_path

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        os.environ["TASKS_FILE_PATH"] = self.test_file
        save_tasks([])

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task = add_task("Test task", 1)
        self.assertEqual(task["description"], "Test task")
        self.assertEqual(task["priority"], 1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)

    def test_delete_task(self):
        add_task("Task to delete", 2)
        tasks = load_tasks()
        task_id = tasks[0]["id"]
        result = delete_task(task_id)
        self.assertTrue(result)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()
