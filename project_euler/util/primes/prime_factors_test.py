from unittest import TestCase

from project_euler.util.primes.prime_factors import prime_factors, prime_factors_int

class TestPrimeFactors(TestCase):
    def test_prime_factors(self):
        self.assertEqual([], list(prime_factors(1)))
        self.assertEqual([2], list(prime_factors(2)))
        self.assertEqual([3], list(prime_factors(3)))
        self.assertEqual([7919], list(prime_factors(7919)))
        self.assertEqual([3, 3, 3, 11, 179, 277, 499], list(prime_factors(7348349349)))

    def test_prime_factors_int(self):
        self.assertEqual([], list(prime_factors_int(1)))
        self.assertEqual([2], list(prime_factors_int(2)))
        self.assertEqual([3], list(prime_factors_int(3)))
        self.assertEqual([7919], list(prime_factors_int(7919)))
        self.assertEqual([15017, 23197], list(prime_factors_int(348349349)))