from itertools import count

from project_euler.util.primes.sieve_of_eratosthenes import RollingSieve
from project_euler.util.sequences.composites import odd_composites

def get_answer() -> int:
    rolling_sieve = RollingSieve()
    for odd_composite in odd_composites():
        rolling_sieve.update_to(odd_composite)
        if not can_be_prime_plus_double_square(odd_composite, rolling_sieve.seen_primes):
            return odd_composite
    return 0

def can_be_prime_plus_double_square(n: int, primes: list) -> bool:
    for prime in primes:
        if prime > n - 2:
            break
        for square in map(lambda x: x * x, count(1)):
            candidate = prime + (2 * square)
            if candidate == n:
                return True
            if candidate > n:
                break
    return False