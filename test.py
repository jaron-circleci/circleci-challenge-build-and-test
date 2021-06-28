import unittest
import requests

class TestMyForm(unittest.TestCase):

    def test_text(self):
        API_URL = "/process"
        r = requests.post(API_URL)
        self.assertTrue(r'CircleCI' in r.text)


if __name__ == "__main__":
    unittest.main()