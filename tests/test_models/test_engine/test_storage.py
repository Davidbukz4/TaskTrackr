#!/usr/bin/python3
"""
Unittest for storage class
"""
import unittest
from unittest.mock import patch
from models.engine.storage import Storage
from models.user import User
from models.task import Task


class TestStorage(unittest.TestCase):
    """ Test cases for db storage"""
    def setUp(self):
        self.storage = Storage()

    def tearDown(self):
        self.storage.close()
        self.storage = None

    @patch('storage.create_engine')
    @patch('storage.sessionmaker')
    def test_init(self, mock_sessionmaker, mock_create_engine):
        self.storage.__init__()
        mock_create_engine.assert_called_once_with('mysql+mysqldb://{}:{}@{}/{}'.format('test_user', 'test_password', 'test_host', 'test_db'))
        mock_sessionmaker.assert_called_once_with(bind=mock_create_engine.return_value, expire_on_commit=False)

    def test_get(self):
        user = User(password='test_password', username='test_user', email='test@example.com')
        self.storage.new(user)
        self.storage.save()
        retrieved_user = self.storage.get(User, user.id)
        self.assertEqual(user, retrieved_user)

    def test_get_invalid_id(self):
        user = self.storage.get(User, 1)
        self.assertIsNone(user)

    def test_getUserObj(self):
        user = User(password='test_password', username='test_user', email='test@example.com')
        self.storage.new(user)
        self.storage.save()
        retrieved_user = self.storage.getUserObj(User, user.username)
        self.assertEqual(user, retrieved_user)

    def test_getUserObj_invalid_username(self):
        user = self.storage.getUserObj(User, 'invalid_username')
        self.assertIsNone(user)

    def test_count(self):
        user1 = User(password='test_password1', username='test_user1', email='test1@example.com')
        user2 = User(password='test_password2', username='test_user2', email='test2@example.com')
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        count = self.storage.count(User)
        self.assertEqual(count, 2)

    def test_all(self):
        user1 = User(password='test_password1', username='test_user1', email='test1@example.com')
        user2 = User(password='test_password2', username='test_user2', email='test2@example.com')
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        all_users = self.storage.all(User)
        self.assertEqual(len(all_users), 2)
        self.assertIn(user1, all_users.values())
        self.assertIn(user2, all_users.values())

    def test_user_tasks(self):
        user = User(password='test_password', username='test_user', email='test@example.com')
        task1 = Task(title='Task 1', description='Task 1 description', due_date='2023-06-30', user_id=user.id)
        task2 = Task(title='Task 2', description='Task 2 description', due_date='2023-06-30', user_id=user.id)
        self.storage.new(user)
        self.storage.new(task1)
        self.storage.new(task2)
        self.storage.save()
        tasks, task_count = self.storage.user_tasks(user.id)
        self.assertEqual(task_count, 2)
        self.assertIn(task1.to_dict(), tasks.values())
        self.assertIn(task2.to_dict(), tasks.values())

    def test_user_info(self):
        user1 = User(password='test_password1', username='test_user1', email='test1@example.com')
        user2 = User(password='test_password2', username='test_user2', email='test2@example.com')
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()
        users = self.storage.user_info()
        self.assertEqual(len(users), 2)
        self.assertIn(user1.to_dict(), users)
        self.assertIn(user2.to_dict(), users)

    def test_new(self):
        user = User(password='test_password', username='test_user', email='test@example.com')
        self.storage.new(user)
        self.storage.save()
        retrieved_user = self.storage.get(User, user.id)
        self.assertEqual(user, retrieved_user)

    def test_delete(self):
        user = User(password='test_password', username='test_user', email='test@example.com')
        self.storage.new(user)
        self.storage.save()
        self.storage.delete(User, user.id)
        deleted_user = self.storage.get(User, user.id)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
