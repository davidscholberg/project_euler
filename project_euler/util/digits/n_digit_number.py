from typing import Iterator

from project_euler.util.iterable.integer_sets import integer_pairs

def max_n_digit_number(n: int) -> int:
    return (10 ** n) - 1

def min_n_digit_number(n: int) -> int:
    if n == 1:
        return 0
    return 10 ** (n - 1)

def unique_pairs_of_n_digit_numbers(n: int) -> Iterator[tuple[int, int]]:
    min_number = min_n_digit_number(n)
    max_number = max_n_digit_number(n)
    yield from integer_pairs(min_number, max_number, distinct=True)