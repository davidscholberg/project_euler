import math
from libcpp.list cimport list
from typing import Iterable

def append_digit(n: int, digit: int) -> int:
    """Append digit to the right of n."""
    return (n * 10) + digit

def digit_count(n: int) -> int:
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

def digit_count_map(n: int) -> tuple[int, int, int, int, int, int, int, int, int, int]:
    """Returns tuple that maps digits to digit counts for the given number."""
    digit_count_map = [0] * 10
    for digit in digits(n):
        digit_count_map[digit] += 1
    return tuple(digit_count_map)

def digital_root(n: int) -> int:
    """Returns the digital root of n."""
    remaining_digits = digits(n)
    while True:
        digits_sum = sum(remaining_digits)
        if digits_sum < 10:
            return digits_sum
        remaining_digits = digits(digits_sum)

def digits(n: int) -> tuple[int]:
    """Individual digits from n in base 10."""
    return tuple(map(int, str(n)))

def digits_c_wrapper(int n) -> tuple[int]:
    """Individual digits from n in base 10. This is a python wrapper for digits_c, mostly intended for unit testing."""
    cdef list[int] digits_list
    digits_c(n, &digits_list)
    return tuple(digits_list)

cdef void digits_c(int n, list[int]* digits_list):
    """Individual digits from n in base 10. Pure cython implementation."""
    if n == 0:
        digits_list.push_front(0)
        return
    while n != 0:
        digits_list.push_front(n % 10)
        n //= 10

def number_from_digits(digits: Iterable[int]) -> int:
    n = 0
    for digit in digits:
        n = (n * 10) + digit
    return n