from itertools import combinations_with_replacement
from typing import Iterator

from project_euler.util.multiples.factors import factors

def abundant_numbers(minimum: int, maximum:int) -> Iterator[int]:
    for n in range(minimum, maximum + 1):
        if sum(factors(n, proper=True)) > n:
            yield n

def non_abundant_sum_numbers(maximum:int) -> Iterator[int]:
    """Return all numbers not equal to the sum of two abundant numbers, capped by given maximum."""
    abundant_number_pair_sums = [False] * (maximum + 1)
    abundant_numbers_tuple = tuple(abundant_numbers(1, maximum))
    for i, j in combinations_with_replacement(range(0, len(abundant_numbers_tuple)), 2):
        pair_sum = abundant_numbers_tuple[i] + abundant_numbers_tuple[j]
        if pair_sum <= maximum:
            abundant_number_pair_sums[pair_sum] = True
    yield from filter(
        lambda n: not abundant_number_pair_sums[n],
        range(1, maximum + 1)
    )