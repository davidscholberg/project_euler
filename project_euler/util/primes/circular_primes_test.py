from unittest import TestCase

from project_euler.util.primes.circular_primes import circular_primes

class TestCircularPrimes(TestCase):
    def test_circular_primes(self):
        self.assertEqual(
            (2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97),
            tuple(circular_primes(99))
        )