import math
from typing import Iterable

class GetDigitsIterator:
    def __init__(self, n: int, reverse: bool = False) -> None:
        self._n = n
        max_digit_power = math.floor(math.log10(self._n))
        if reverse:
            self._digit_power = 0
            self._digit_power_out_of_bounds = lambda x: x > max_digit_power
            self._digit_power_update_value = lambda x: x + 1
        else:
            self._digit_power = max_digit_power
            self._digit_power_out_of_bounds = lambda x: x < 0
            self._digit_power_update_value = lambda x: x - 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._digit_power_out_of_bounds(self._digit_power):
            raise StopIteration
        current_digit = (self._n // (10 ** self._digit_power)) % 10
        self._digit_power = self._digit_power_update_value(self._digit_power)
        return current_digit

def get_first_x_digits(n: int, x: int) -> int:
    return n // (10 ** (get_number_of_digits(n) - x))

def get_number_from_digits(digits: Iterable[int]) -> int:
    n = 0
    for i, digit in enumerate(digits):
        power_of_ten = len(digits) - 1 - i
        n += digit * (10 ** power_of_ten)
    return n

def get_number_of_digits(n: int) -> int:
    return math.floor(math.log10(n)) + 1

def is_palindromic_number(n: int) -> bool:
    if n < 10:
        return True
    reverse_n = 0
    for digit in GetDigitsIterator(n, reverse = True):
        reverse_n = (reverse_n * 10) + digit
    return reverse_n == n