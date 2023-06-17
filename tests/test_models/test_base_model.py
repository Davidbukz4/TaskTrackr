#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test the base model class
    """
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        self.base_model = None

    def test_save(self):
        self.assertIsNone(self.base_model['updated_at'])
        self.base_model.save()
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict(self):
        expected_keys = ['__class__']
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(expected_keys, obj_dict.keys())

        # Test if created_at and updated_at are formatted as ISO strings
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
