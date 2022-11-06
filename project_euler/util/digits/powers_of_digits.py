from itertools import repeat, starmap
from typing import Iterator

from project_euler.util.digits.digits import digits

def powers_of_digits(n: int, power: int) -> Iterator[int]:
    yield from starmap(pow, zip(digits(n), repeat(power)))