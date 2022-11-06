from itertools import count
from typing import Iterator

from project_euler.util.digits.n_digit_number import max_n_digit_number, min_n_digit_number
from project_euler.util.digits.powers_of_digits import powers_of_digits

def numbers_equal_to_sum_of_powers_of_digits(power: int) -> Iterator[int]:
    for digit_count in count(start=2):
        minimum = min_n_digit_number(digit_count)
        maximum = max_n_digit_number(digit_count)
        max_sum_of_digit_powers = sum(powers_of_digits(maximum, power))
        if minimum > max_sum_of_digit_powers:
            break
        for n in range(minimum, maximum + 1):
            if n > max_sum_of_digit_powers:
                break
            if n == sum(powers_of_digits(n, power)):
                yield n