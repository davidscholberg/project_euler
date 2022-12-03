from typing import Iterable

from project_euler.util.digits.digits import digits, number_from_digits

def max_pandigital(digit_count: int) -> int:
    return number_from_digits(range(digit_count, 0, -1))

def min_pandigital(digit_count: int) -> int:
    return number_from_digits(range(1, digit_count + 1))

def is_pandigital(n: int | Iterable[int]) -> bool:
    if isinstance(n, int):
        n = digits(n)
    digit_tuple = tuple(n)
    digit_map = [False] * (len(digit_tuple) + 1)
    for digit in digit_tuple:
        if digit == 0:
            return False
        if digit >= len(digit_map):
            return False
        if digit_map[digit]:
            return False
        digit_map[digit] = True
    return True