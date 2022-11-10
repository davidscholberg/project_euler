from typing import Iterable, Iterator

from project_euler.util.digits.base_convert import base_convert
from project_euler.util.digits.palindrome import is_palindromic_number

def get_answer() -> int:
    total = 0
    for n in range(1, 1000000):
        if n % 10 == 0:
            continue
        if is_palindromic_number(n) and is_palindromic_number(base_convert(n, 10, 2)):
            total += n
    return total