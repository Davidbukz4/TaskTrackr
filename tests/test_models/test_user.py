#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from models.user import User

class TestUserModel(unittest.TestCase):
    """Class for testing User Class"""
    def setUp(self):
        self.password = "password"
        self.username = "test_user"
        self.email = "test@example.com"
        self.user = User(self.password, self.username, self.email)

    def tearDown(self):
        self.user = None

    def test_password_hashing(self):
        self.assertNotEqual(self.password, self.user.password)
        self.assertTrue(self.user.check_password(self.password))

    def test_username(self):
        self.assertEqual(self.username, self.user.username)

    def test_email(self):
        self.assertEqual(self.email, self.user.email)

    def test_to_dict(self):
        expected_keys = ['__class__', 'id', 'password', 'username', 'email']
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertCountEqual(expected_keys, user_dict.keys())

if __name__ == '__main__':
    unittest.main()
