import math

from project_euler.util.arithmetic.polynomial import polynomial
from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.iterable.nth import nth

def base_convert(n: int, from_base: int, to_base: int) -> int:
    """Convert number between any base from 2 through 10."""
    if from_base != 10:
        n = nth(1, polynomial(tuple(digits(n)), (from_base,)))
    max_exponent = math.floor(math.log(n, to_base))
    to_digits = []
    for exponent in range(max_exponent, -1, -1):
        power = to_base ** exponent
        digit = n // power
        to_digits.append(digit)
        n -= (digit * power)
    return number_from_digits(to_digits)