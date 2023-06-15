#!/usr/bin/python3
"""
Unit Test for Task Class
"""
import unittest
from models.task import Task

class TestTaskModel(unittest.TestCase):
    """Class for testing Task class"""
    def setUp(self):
        self.title = "Test Task"
        self.description = "This is a test task."
        self.due_date = "2023-06-30"
        self.user_id = 1
        self.task = Task(self.title, self.description,
                         self.due_date, self.user_id)

    def tearDown(self):
        self.task = None

    def test_title(self):
        self.assertEqual(self.title, self.task.title)

    def test_description(self):
        self.assertEqual(self.description, self.task.description)

    def test_completed_default(self):
        self.assertFalse(self.task.completed)

    def test_due_date(self):
        self.assertEqual(self.due_date, self.task.due_date)

    def test_user_id(self):
        self.assertEqual(self.user_id, self.task.user_id)

    def test_created_at(self):
        self.assertIsNotNone(self.task.created_at)

    def test_updated_at(self):
        self.assertIsNotNone(self.task.updated_at)

    def test_update_updated_at(self):
        old_updated_at = self.task.updated_at
        self.task.title = "Updated Title"
        self.assertNotEqual(old_updated_at, self.task.updated_at)

    def test_to_dict(self):
        expected_keys = ['__class__', 'id', 'title', 'description',
                         'completed', 'user_id', 'created_at',
                         'updated_at', 'due_date']
        task_dict = self.task.to_dict()
        self.assertIsInstance(task_dict, dict)
        self.assertCountEqual(expected_keys, task_dict.keys())

if __name__ == '__main__':
    unittest.main()
