from itertools import count, product
import math

from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.primes.polynomial_primes import polynomial_primes
from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

def get_answer() -> int:
    coefficient_sets = product((1,), range(-999, 1000), sieve_of_eratosthenes(1000))
    consecutive_prime_counts = map(
        lambda coefficient_set: (coefficient_set, iter_len(polynomial_primes(coefficient_set, count(start=1)))),
        coefficient_sets
    )
    coefficients_with_max_prime_count = max(consecutive_prime_counts, key=lambda t: t[1])[0]
    return math.prod(coefficients_with_max_prime_count)