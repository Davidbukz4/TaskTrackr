#!/usr/bin/python3
import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_error_handler_404(self):
        response = self.app.get('/invalid_endpoint')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Not found'})

if __name__ == '__main__':
    unittest.main()
