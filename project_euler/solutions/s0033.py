from functools import reduce

from project_euler.util.digits.digits import digits
from project_euler.util.fractions.divide import divide
from project_euler.util.fractions.multiply import multiply_fractions
from project_euler.util.fractions.reduce import reduce_fraction
from project_euler.util.iterable.integer_sets import integer_pairs

def get_answer() -> int:
    digit_cancelling_fractions = []
    for a, b in integer_pairs(11, 99, distinct=True):
        if a % 10 == 0 or b % 10 == 0:
            continue
        a_digits = tuple(digits(a))
        b_digits = tuple(digits(b))
        for i in range(0, 2):
            digit_to_cancel = a_digits[i]
            try:
                b_i = b_digits.index(digit_to_cancel)
            except ValueError:
                continue
            cancelled_a = a_digits[not i]
            cancelled_b = b_digits[not b_i]
            if divide(a, b) == divide(cancelled_a, cancelled_b):
                digit_cancelling_fractions.append((a, b))
    product = reduce(multiply_fractions, digit_cancelling_fractions)
    return reduce_fraction(product)[1]