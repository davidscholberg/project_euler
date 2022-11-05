from unittest import TestCase

from project_euler.util.arithmetic.polynomial import polynomial

class TestPolynomial(TestCase):
    def test_polynomial(self):
        self.assertEqual((1, 1, 1, 1, 1), tuple(polynomial((1,), range(0, 5))))
        self.assertEqual((9, 14, 19, 24, 29), tuple(polynomial((5, 9), range(0, 5))))
        self.assertEqual((6, 11, 20, 33, 50), tuple(polynomial((2, 3, 6), range(0, 5))))