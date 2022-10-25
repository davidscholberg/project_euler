from typing import Iterator

# see sieve of eratosthenes
def prime_factors(n: int) -> Iterator[int]:
    potential_prime_factor = 2
    while n > 1:
        if n % potential_prime_factor == 0:
            yield potential_prime_factor
            n //= potential_prime_factor
        else:
            potential_prime_factor += 1
