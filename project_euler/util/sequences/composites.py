from typing import Iterator

from project_euler.util.primes.is_prime import is_prime

def odd_composites() -> Iterator[int]:
    current = 9
    while True:
        yield current
        current += 2
        while is_prime(current):
            current += 2