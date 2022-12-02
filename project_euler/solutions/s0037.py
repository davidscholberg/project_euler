from itertools import chain
from typing import Iterator

from project_euler.util.digits.digits import append_digit
from project_euler.util.primes.is_prime import is_prime
from project_euler.util.primes.truncatable_prime import is_left_truncatable_prime

left_digits = (2, 3, 5, 7)
"""Digits that are valid leftmost digits for left-truncatable and right-truncatable primes."""

middle_and_end_digits = (1, 3, 7, 9)
"""Digits that are valid middle and end digits for left-truncatable and right-truncatable primes."""

def left_and_right_truncatable_primes(right_truncatable_prime: int) -> Iterator[int]:
    """Yield set of left-truncatable and right-truncatable primes, using the input number as a seed to generate right-truncatable primes.

    The input number itself is not yielded.
    """
    for digit in middle_and_end_digits:
        candidate = append_digit(right_truncatable_prime, digit)
        if not is_prime(candidate):
            continue
        if is_left_truncatable_prime(candidate):
            yield candidate
        yield from left_and_right_truncatable_primes(candidate)

def get_answer() -> int:
    return sum(chain.from_iterable(map(left_and_right_truncatable_primes, left_digits)))