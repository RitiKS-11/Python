import unittest

from pkg.req import check_connection

class TestConnection(unittest.TestCase):
    def test_connect_google(self):
        response = check_connection('https://www.google.com')
        self.assertEqual( response, "Connected", \
                         "Resutl should be connected.")
        
    def test_random_url(self):
        response = check_connection('https://www.goog.com')
        self.assertEqual( response, 'Not connected', \
                         'Result should be not connected.')
        

if __name__ == "__main__":
    unittest.main()
