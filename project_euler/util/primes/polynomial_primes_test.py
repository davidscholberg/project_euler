from itertools import count
from unittest import TestCase

from project_euler.util.primes.polynomial_primes import polynomial_primes

class TestPolynomialPrimes(TestCase):
    def test_polynomial_primes(self):
        self.assertEqual((), tuple(polynomial_primes((1, 2, 4), count())))
        self.assertEqual((2, 5), tuple(polynomial_primes((1, 2, 2), count())))
        self.assertEqual((3, 7, 17), tuple(polynomial_primes((3, 1, 3), count())))