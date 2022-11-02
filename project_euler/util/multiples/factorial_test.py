from unittest import TestCase

from project_euler.util.multiples.factorial import factorial

class TestFactorial(TestCase):
    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(2, factorial(2))
        self.assertEqual(6, factorial(3))
        self.assertEqual(24, factorial(4))
        self.assertEqual(120, factorial(5))
        self.assertEqual(720, factorial(6))
        self.assertEqual(5040, factorial(7))
        self.assertEqual(40320, factorial(8))
        self.assertEqual(362880, factorial(9))
        self.assertEqual(3628800, factorial(10))