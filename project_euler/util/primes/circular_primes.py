from typing import Any, Iterable, Iterator

from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.primes.is_prime import is_prime
from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes
from project_euler.util.sequences.rotations import rotations

def circular_primes(limit: int) -> Iterator[int]:
    """Return primes for which each 1-digit rotation is also prime."""
    cache: list[None | bool] = [None] * (limit + 1)
    def add_rotations_to_cache(rotations: Iterable[tuple[Any]], value: bool) -> None:
        for rotation in rotations:
            cache[number_from_digits(rotation)] = value
    for prime in sieve_of_eratosthenes(limit):
        if prime < 10:
            yield prime
            continue
        if cache[prime] is not None:
            if cache[prime]:
                yield prime
            continue
        digits_tuple = tuple(digits(prime))
        rotations_tuple = tuple(rotations(digits_tuple))
        circular = True
        for digit in digits_tuple:
            if digit % 2 == 0:
                circular = False
                break
        if not circular:
            add_rotations_to_cache(rotations_tuple, False)
            continue
        for rotation in rotations(digits_tuple):
            if not is_prime(number_from_digits(rotation)):
                circular = False
                break
        if not circular:
            add_rotations_to_cache(rotations_tuple, False)
            continue
        yield prime
        add_rotations_to_cache(rotations_tuple, True)