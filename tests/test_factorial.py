import unittest

from pkg.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_true_factorial(self):
        self.assertEqual(factorial(6), 720, 'Should be 720')

    def test_wrong_factorial(self):
        self.assertNotEqual(factorial(1), 11, 'Should be 1')

    def test_factorial_of_100(self):
        self.assertEqual(factorial(100), 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000 )