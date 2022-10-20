from unittest import TestCase

from project_euler.util.primes.prime_factors import prime_factors

class TestPrimeFactors(TestCase):
    def test_prime_factors(self):
        self.assertEqual([], list(prime_factors(1)))
        self.assertEqual([2], list(prime_factors(2)))
        self.assertEqual([3], list(prime_factors(3)))
        self.assertEqual([7919], list(prime_factors(7919)))
        self.assertEqual([3, 3, 3, 11, 179, 277, 499], list(prime_factors(7348349349)))