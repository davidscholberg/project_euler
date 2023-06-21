from itertools import count
from typing import Iterator

from project_euler.util.digits.n_digit_number import max_n_digit_number, min_n_digit_number
from project_euler.util.iterable.iter_len import iter_len

def n_digit_powers(digit_count: int, exponent: int) -> Iterator[int]:
    """
    Returns powers of the given exponent that have the given number of digits.
    """
    powers = map(lambda n: n ** exponent, count(1))
    smallest_n_digit_number = min_n_digit_number(digit_count)
    largest_n_digit_number = max_n_digit_number(digit_count)
    for power in powers:
        if power > largest_n_digit_number:
            break
        if power >= smallest_n_digit_number:
            yield power

def get_answer() -> int:
    n_digits_nth_power_count = 0
    for digit_count in count(1):
        if 9 ** digit_count < min_n_digit_number(digit_count):
            break
        n_digits_nth_power_count += iter_len(n_digit_powers(digit_count, digit_count))
    return n_digits_nth_power_count