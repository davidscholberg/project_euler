from itertools import count

from project_euler.util.digits.digits import digits
from project_euler.util.digits.n_digit_number import max_n_digit_number, min_n_digit_number
from project_euler.util.multiples.factorial import factorial

def get_answer() -> int:
    factorial_cache = {}
    factorial_using_cache = lambda n: factorial(n, cache=factorial_cache)
    max_digit_factorial = lambda digit_count: 362880 * digit_count
    digit_factorials_sum = 0
    for digit_count in count(start=2):
        max_n = max_n_digit_number(digit_count)
        min_n = min_n_digit_number(digit_count)
        max_digit_factorial_of_digit_count = max_digit_factorial(digit_count)
        if min_n > max_digit_factorial_of_digit_count:
            break
        for n in range(min_n, max_n + 1):
            if n > max_digit_factorial_of_digit_count:
                break
            if n == sum(map(factorial_using_cache, digits(n))):
                digit_factorials_sum += n
    return digit_factorials_sum