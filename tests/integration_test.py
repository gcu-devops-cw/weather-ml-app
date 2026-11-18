import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


class TestIntegration(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_prediction_flow(self):
        form_data = {
            'temperature': '280.0',
            'pressure': '1012',
            'humidity': '75',
            'wind_speed': '3.5',
            'wind_deg': '180',
            'rain_1h': '0',
            'rain_3h': '0',
            'snow': '0',
            'clouds': '20',
        }

        response = self.client.post('/', data=form_data)
        self.assertEqual(response.status_code, 200)

        html_text = response.data.decode('utf-8').lower()

        # Ensure that the result page (response.data) should include a weather prediction
        self.assertIn('the weather is:', html_text)

        # Ensure that the result page should include a prediction time
        self.assertIn('prediction time:', html_text)
        self.assertIn('ms', html_text)

        valid_classes = [
            'clear', 'cloudy', 'drizzly', 'foggy', 'hazey',
            'misty', 'rainy', 'smokey', 'thunderstorm',
        ]
        found = any(weather in html_text for weather in valid_classes)

        # Ensure that classification is in valid classes, provide an error message if not.
        self.assertTrue(
            found,
            f"Classification is not in valid weather classes {valid_classes}. Response was: {html_text}",
        )


if __name__ == '__main__':
    unittest.main()
