from itertools import count

from project_euler.util.digits.n_digit_number import max_n_digit_number, min_n_digit_number
from project_euler.util.sums.digit_factorial_sum import digit_factorial_sum

def get_answer() -> int:
    digit_factorials_sum = 0
    for digit_count in count(start=2):
        max_n = max_n_digit_number(digit_count)
        min_n = min_n_digit_number(digit_count)
        max_digit_factorial_sum = 362880 * digit_count
        if min_n > max_digit_factorial_sum:
            break
        for n in range(min_n, min(max_n, max_digit_factorial_sum) + 1):
            if n == digit_factorial_sum(n):
                digit_factorials_sum += n
    return digit_factorials_sum