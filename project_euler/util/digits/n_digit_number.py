from itertools import combinations
from typing import Iterator

def max_n_digit_number(n: int) -> int:
    return (10 ** n) - 1

def min_n_digit_number(n: int) -> int:
    if n == 1:
        return 0
    return 10 ** (n - 1)

def unique_pairs_of_n_digit_numbers(n: int) -> Iterator[tuple[int, int]]:
    min_number = min_n_digit_number(n)
    max_number = max_n_digit_number(n)
    yield from combinations(range(min_number, max_number + 1), 2)