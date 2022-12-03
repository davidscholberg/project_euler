from itertools import count
from typing import Final

from project_euler.util.digits.concatenated_product import concatenated_product
from project_euler.util.digits.pandigital import is_pandigital

def get_answer() -> int:
    max_possible_pandigital: Final[int] = 987654321
    max_pandigital = 0
    for multiplier_cap in range(2, 10):
        multipliers = tuple(range(1, multiplier_cap + 1))
        for n in count(1):
            candidate = concatenated_product(n, multipliers)
            if candidate > max_possible_pandigital:
                break
            if is_pandigital(candidate) and candidate > max_pandigital:
                max_pandigital = candidate
    return max_pandigital