import math

from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

def nth_prime(n: int) -> int:
    prime_count = 0
    upper_bound = 11
    if n >= 6:
        upper_bound = n * math.ceil(math.log(n) + math.log(math.log(n)))
    for prime in sieve_of_eratosthenes(upper_bound):
        prime_count += 1
        if prime_count == n:
            return prime