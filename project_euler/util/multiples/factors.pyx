from itertools import chain
from libcpp.list cimport list
import math
from typing import Iterator

def factors(int n, proper: bool = False) -> tuple[int]:
    cdef list[int] factors_list
    factors_list.push_back(1)
    cdef int i, partner
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            factors_list.push_back(i)
            partner = n // i
            if partner != i:
                factors_list.push_back(partner)
    if not proper and n > 1:
        factors_list.push_back(n)
    return tuple(factors_list)

def amicable_numbers(minimum: int, maximum:int) -> Iterator[int]:
    yield from chain.from_iterable(amicable_pairs(minimum, maximum))

def amicable_pairs(minimum: int, maximum:int) -> Iterator[tuple[int, int]]:
    factors_sum_cache = {}
    amicable_cache = {}
    def sum_of_factors(n: int) -> int:
        if n in factors_sum_cache:
            return factors_sum_cache[n]
        s = sum(factors(n, proper=True))
        factors_sum_cache[n] = s
        return s
    for n in range(minimum, maximum + 1):
        if n in amicable_cache:
            continue
        candidate = sum_of_factors(n)
        if n == candidate:
            amicable_cache[n] = False
            continue
        if n != sum_of_factors(candidate):
            amicable_cache[n] = False
            continue
        yield (n, candidate)
        amicable_cache[n] = True
        amicable_cache[candidate] = True

def is_amicable_pair(a: int, b: int) -> bool:
    return (
        a != b and
        a == sum(factors(b, proper=True)) and
        b == sum(factors(a, proper=True))
    )