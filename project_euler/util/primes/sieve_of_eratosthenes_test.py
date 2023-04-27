from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.primes.sieve_of_eratosthenes import RollingSieve, sieve_of_eratosthenes

class TestSieveOfEratosthenes(TestCase):
    def test_rolling_sieve(self):
        self.assertEqual([2, 3, 5, 7], list(count_cap(4, RollingSieve(chunk_size=10))))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71], list(count_cap(20, RollingSieve(chunk_size=5))))
        rolling_sieve = RollingSieve(chunk_size=5)
        rolling_sieve.update_to(3)
        self.assertEqual([2, 3], rolling_sieve.seen_primes)
        rolling_sieve.update_to(4)
        self.assertEqual([2, 3, 5], rolling_sieve.seen_primes)
        rolling_sieve.update_to(10)
        self.assertEqual([2, 3, 5, 7, 11], rolling_sieve.seen_primes)
        rolling_sieve.update_to(14)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17], rolling_sieve.seen_primes)
        rolling_sieve.update_to(15)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17], rolling_sieve.seen_primes)
        rolling_sieve.update_to(17)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17], rolling_sieve.seen_primes)
        rolling_sieve.update_to(21)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23], rolling_sieve.seen_primes)


    def test_sieve_of_eratosthenes(self):
        self.assertEqual([2, 3, 5, 7], list(sieve_of_eratosthenes(10)))
        self.assertEqual([2, 3, 5, 7, 11], list(sieve_of_eratosthenes(11)))
        self.assertEqual([2, 3, 5, 7, 11], list(sieve_of_eratosthenes(12)))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71], list(sieve_of_eratosthenes(71)))