import math
from typing import Iterable, Iterator

def digit_count(n: int) -> int:
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

def digits(n: int, reverse: bool = False) -> Iterator[int]:
    if n < 10:
        yield n
        return
    max_digit_power = math.floor(math.log10(n))
    digit_power = None
    digit_power_out_of_bounds = None
    digit_power_update = None
    if reverse:
        digit_power = 0
        digit_power_out_of_bounds = lambda x: x > max_digit_power
        digit_power_update = lambda x: x + 1
    else:
        digit_power = max_digit_power
        digit_power_out_of_bounds = lambda x: x < 0
        digit_power_update = lambda x: x - 1
    while not digit_power_out_of_bounds(digit_power):
        yield (n // (10 ** digit_power)) % 10
        digit_power = digit_power_update(digit_power)

def number_from_digits(digits: Iterable[int]) -> int:
    n = 0
    for digit in digits:
        n = (n * 10) + digit
    return n