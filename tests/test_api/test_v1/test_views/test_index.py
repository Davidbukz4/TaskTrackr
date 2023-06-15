#!/usr/bin/python3
"""
Unittest for index module
"""
import unittest
from flask import Flask
from flask.testing import FlaskClient
from api.v1.app import (app)

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_status_endpoint(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'OK'})

    def test_stats_users_endpoint(self):
        response = self.app.get('/stats/users')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
