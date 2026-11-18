import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


class SmokeTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    # Complete the function below to test a success in running the application
    def test_prediction_route_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Complete the function below to test a form is rendered
    def test_form_is_rendered(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html_text = response.data.decode('utf-8').lower()
        self.assertIn('<form', html_text)
        self.assertIn('name="temperature"', html_text)


if __name__ == '__main__':
    unittest.main()
