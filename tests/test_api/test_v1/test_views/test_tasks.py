#!/usr/bin/python3
"""
Test for task api
"""
import unittest
from flask import jsonify
from api.v1.app import (app)


class TaskEndpointsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_all_task_endpoint(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_task_by_id_endpoint(self):
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)

    def test_user_tasks_endpoint(self):
        response = self.app.get('/tasks/user/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_task_endpoint(self):
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)

    def test_post_task_endpoint(self):
        data = {
            'title': 'Task 1',
            'description': 'Description of Task 1',
            'due_date': '2023-06-30'
        }
        response = self.app.post('/tasks/1', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_task_endpoint(self):
        data = {
            'title': 'Updated Task',
            'description': 'Updated description',
            'due_date': '2023-07-15'
        }
        response = self.app.put('/tasks/1', json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
