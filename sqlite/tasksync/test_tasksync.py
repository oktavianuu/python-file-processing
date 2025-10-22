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
            self.app.add_task("", 1)
        self.assertEqual(str(context.exception), "Task name cannot be empty")
    
    def test_add_task_priority_less_than_one(self):
        """Test adding task with invalid priority"""
        with self.assertRaises(ValueError) as context:
            self.app.add_task("Test Task", 0)
        self.assertEqual(str(context.exception), "Priority must be at least 1")        

    def test_add_duplicate_task(self):
        """Test finding a task that doesn't exist"""
        self.app.add_task("Duplicate Task", 2)

        with self.assertRaises(ValueError) as context:
            self.app.add_task("Duplicate Task", 2)
        self.assertEqual(str(context.exception), "Task with this name already exists")

    def test_find_nonexistent_task(self):
        """Test finding a task that doesn't exist"""
        task = self.app.find_task("Non Existent")
        self.assertIsNone(task)

    def test_show_tasks_empty(self):
        task = self.app.show_tasks()
        self.assertEqual(task, [])
    
    def test_show_task_with_data(self):
        """Test showing task with data"""
        self.app.add_task("Task 1", 1)
        self.app.add_task("Task 2", 2)

        tasks = self.app.show_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['name'], "Task 1")
        self.assertEqual(tasks[1]['name'], "Task 2")

class TestTaskSyncIntegration(unittest.TestCase):
    """Integration test with actual user input simulation"""
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)
    
    def full_workflow(self):
        """Test complete user workflow"""
        app = TaskSync(self.db_path)

        # add mul task
        app.add_task("wrk", 1)
        app.add_task("std", 2)

        # verify they exxist
        tasks = app.show_tasks()
        self.assertEqual(len(tasks), 2)

        # find specific task
        task = app.find_task("Study")
        self.assertEqual(task['priority'], 2)

        app.close()

if __name__ == "__main__":
    # Run with detailed output
    unittest.main(verbosity=2)