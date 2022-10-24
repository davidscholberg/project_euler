from unittest import TestCase

from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

class TestSieveOfEratosthenes(TestCase):
    def test_sieve_of_eratosthenes(self):
        self.assertEqual([2, 3, 5, 7], list(sieve_of_eratosthenes(10)))
        self.assertEqual([2, 3, 5, 7, 11], list(sieve_of_eratosthenes(11)))
        self.assertEqual([2, 3, 5, 7, 11], list(sieve_of_eratosthenes(12)))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71], list(sieve_of_eratosthenes(71)))