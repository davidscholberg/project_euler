from itertools import chain, repeat, starmap
from operator import mul
from typing import Iterable

from project_euler.util.digits.digits import digits, number_from_digits

def concatenated_product(n: int, multipliers: Iterable[int]) -> int:
    """Concatenation of n times each of the given multipliers."""
    products = starmap(mul, zip(repeat(n), multipliers))
    return number_from_digits(chain.from_iterable(map(digits, products)))