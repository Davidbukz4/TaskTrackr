#!/usr/bin/python3
import unittest
from flask import jsonify
from api.v1.app import (app)


class UserEndpointsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_all_user_endpoint(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_user_by_id_endpoint(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_user_endpoint(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_post_user_endpoint(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'password123'
        }
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_user_endpoint(self):
        data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com'
        }
        response = self.app.put('/users/1', json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
