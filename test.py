import unittest
from math import isclose
from fun import *

class TestMathFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 12)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-1)  # Should raise an error

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(7, 1), 7)
        with self.assertRaises(ValueError):
            power(3, -1)  # Should raise an error

    def test_sqrt(self):
        self.assertTrue(isclose(sqrt(4), 2.0))
        self.assertTrue(isclose(sqrt(9), 3.0))
        with self.assertRaises(ValueError):
            sqrt(-4)  # Should raise an error

    def test_natural_log(self):
        self.assertTrue(isclose(natural_log(1), 0.0))
        self.assertTrue(isclose(natural_log(math.e), 1.0))
        with self.assertRaises(ValueError):
            natural_log(0)  # Should raise an error
        with self.assertRaises(ValueError):
            natural_log(-5)  # Should raise an error

if __name__ == "__main__":
    unittest.main()
