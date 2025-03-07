"""Unit test for app.py"""
import unittest
from app import app

class TestApp(unittest.TestCase):
    """Unit tests for Flask app"""

    def setUp(self):
        """Setup test client"""
        self.client = app.test_client()

    def test_hello_world(self):
        """Test if the endpoint returns Hello, World!"""
        response = self.client.get('/')
        self.assertEqual(response.data.decode(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()

