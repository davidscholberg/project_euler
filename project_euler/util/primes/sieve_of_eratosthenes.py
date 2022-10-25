from typing import Iterator

from project_euler.util.iterable.value_cap import value_cap
from project_euler.util.multiples.multiples import multiples

def sieve_of_eratosthenes(limit: int) -> Iterator[int]:
    composites = [False] * (limit + 2)
    current_prime = 2
    while current_prime <= limit:
        yield current_prime
        for multiple in value_cap(multiples(current_prime, minimum=current_prime * 2), limit):
            composites[multiple] = True
        current_prime += 1
        while composites[current_prime]:
            current_prime += 1