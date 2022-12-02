import math
from typing import Iterable, Iterator

def append_digit(n: int, digit: int) -> int:
    """Append digit to the right of n."""
    return (n * 10) + digit

def digit_count(n: int) -> int:
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

def digits(n: int) -> tuple[int]:
    """Individual digits from n in base 10."""
    return tuple(map(int, str(n)))

def number_from_digits(digits: Iterable[int]) -> int:
    n = 0
    for digit in digits:
        n = (n * 10) + digit
    return n