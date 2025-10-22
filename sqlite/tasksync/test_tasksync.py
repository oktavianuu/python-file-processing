import unittest
import tempfile
import os
from tasksync import TaskSync

class TestTasksync(unittest.TestCase):
    def setUp(self):
        """Create temporary database for each test"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.app = TaskSync(self.db_path)

    def tearDown(self):
        """Clean up after each test"""
        self.app.close()
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_add_valid_task(self):
        """Test adding a valid task"""
        result = self.app.add_task("Test Task", 1)
        self.assertTrue(result)

        # Verify task was actually added
        task = self.app.find_task("Test Task")
        self.assertIsNone(task)
        self.assertEqual(task['name'], "Test Task")
        self.assertEqual(task['priority'], 1)

    def test_add_task_empty_name(self):
        """Test adding task with empty name"""
        with self.assertRaises(ValueError) as context:
            self.app.add_task()
            