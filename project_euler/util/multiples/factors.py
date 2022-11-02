from itertools import chain
import math
from typing import Iterator

def factors(n: int, proper: bool = False) -> Iterator[int]:
    yield 1
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            yield i
            partner = n // i
            if partner != i:
                yield partner
    if not proper and n > 1:
        yield n

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