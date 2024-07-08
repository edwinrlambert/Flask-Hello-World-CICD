import unittest
from flask import url_for
from app import create_app

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Set up test client before each test.
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        
    def test_home_status_code(self):
        # Test that the homepage is accessible.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_data(self):
        # Test the data returned by the home page.
        response = self.client.get('/')
        self.assertIn(b'Hello CI/CD!', response.data)
        
        
if __name__ =="__main__":
    unittest.main()
