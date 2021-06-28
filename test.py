import unittest
import requests
import app

class TestMyForm(unittest.TestCase):
    
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
        
    def test_text(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertTrue(response.data, "CircleCI!" )
    
if __name__ == "__main__":
    unittest.main()