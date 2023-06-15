from itertools import chain, repeat

from project_euler.util.digits.digits import digits
from project_euler.util.fractions.continued_fraction import ContinuedFraction

def get_answer() -> int:
    get_a_terms = lambda: repeat(1)
    get_b_terms = lambda: chain((1,), repeat(2))
    continued_fraction = ContinuedFraction(get_a_terms, get_b_terms, starting_cache_depth=1)
    total = 0
    for depth in range(1000):
        (numerator, denominator) = continued_fraction.calculate(depth)
        if len(digits(numerator)) > len(digits(denominator)):
            total += 1
    return total