from unittest import TestCase

from project_euler.util.primes.nth_prime import nth_prime

class TestNthPrime(TestCase):
    def test_nth_prime(self):
        self.assertEqual(2, nth_prime(1))
        self.assertEqual(3, nth_prime(2))
        self.assertEqual(5, nth_prime(3))
        self.assertEqual(7, nth_prime(4))
        self.assertEqual(11, nth_prime(5))
        self.assertEqual(13, nth_prime(6))
        self.assertEqual(17, nth_prime(7))
        self.assertEqual(19, nth_prime(8))
        self.assertEqual(23, nth_prime(9))
        self.assertEqual(29, nth_prime(10))
        self.assertEqual(7919, nth_prime(1000))