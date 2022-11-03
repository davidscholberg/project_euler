import math

from project_euler.util.iterable.nth import nth
from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

def nth_prime(n: int) -> int:
    upper_bound = 11
    if n >= 6:
        upper_bound = n * math.ceil(math.log(n) + math.log(math.log(n)))
    return nth(n, sieve_of_eratosthenes(upper_bound))