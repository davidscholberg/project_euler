from typing import Iterator

from project_euler.util.iterable.integer_sets import integer_pairs
from project_euler.util.multiples.factors import factors

def abundant_numbers(minimum: int, maximum:int) -> Iterator[int]:
    for n in range(minimum, maximum + 1):
        if sum(factors(n, proper=True)) > n:
            yield n

def numbers_not_sum_of_two_abundant_numbers(maximum:int) -> Iterator[int]:
    abundant_number_pair_sums = [False] * (maximum + 1)
    abundant_numbers_tuple = tuple(abundant_numbers(1, maximum))
    for i, j in integer_pairs(0, len(abundant_numbers_tuple) - 1, distinct=False):
        pair_sum = abundant_numbers_tuple[i] + abundant_numbers_tuple[j]
        if pair_sum <= maximum:
            abundant_number_pair_sums[pair_sum] = True
    yield from filter(
        lambda n: not abundant_number_pair_sums[n],
        range(1, maximum + 1)
    )