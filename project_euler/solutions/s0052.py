from itertools import count

from project_euler.util.digits.digit_permutation import is_digit_permutation
from project_euler.util.digits.n_digit_number import max_n_digit_number, min_n_digit_number

def get_answer() -> int:
    for digit_count in count(2):
        smallest_n_digit_number = min_n_digit_number(digit_count)
        range_cap = (max_n_digit_number(digit_count) // 6) + 1
        for n in range(smallest_n_digit_number, range_cap):
            found = True
            for multiplier in range(2, 7):
                if not is_digit_permutation(n, n * multiplier):
                    found = False
                    break
            if found:
                return n