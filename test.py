import unittest
import requests
from . app import my_form_post

class TestMyForm(unittest.TestCase):
    '''
    def setUp(self):
        self.app = my_form_post.test_client()
        self.app.testing = True
    '''
    def test_text(self):
        API_URL = " http://127.0.0.1:5000/process"
        r = requests.post(API_URL)
        self.assertTrue(r'CircleCI' in r.text)
    '''
    def text_text_1(self):
        circleci_message = 'CircleCi!'
        self.assertEqual(self.my_form_post(), circleci_message)
    '''
if __name__ == "__main__":
    unittest.main()