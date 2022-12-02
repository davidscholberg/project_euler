from unittest import TestCase

from project_euler.util.primes.truncatable_prime import is_left_truncatable_prime, is_right_truncatable_prime

class TestTruncatablePrime(TestCase):
    def test_is_left_truncatable_prime(self):
        self.assertTrue(is_left_truncatable_prime(662617))
        self.assertFalse(is_left_truncatable_prime(11))
        self.assertFalse(is_left_truncatable_prime(222))

    def test_is_right_truncatable_prime(self):
        self.assertTrue(is_right_truncatable_prime(593933))
        self.assertFalse(is_right_truncatable_prime(17))
        self.assertFalse(is_right_truncatable_prime(222))