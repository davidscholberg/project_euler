from functools import reduce

from ..util.decimals import divide, multiply_fractions, reduce_fraction
from ..util.digits import GetDigitsIterator, has_digit, remove_digit

def get_answer() -> int:
    digit_cancelling_fractions = []
    for a in range(10, 99):
        for b in range(a + 1, 100):
            for a_digit in GetDigitsIterator(a):
                if has_digit(b, a_digit):
                    reduced_a = remove_digit(a, a_digit)
                    reduced_b = remove_digit(b, a_digit)
                    if reduced_a == 0 or reduced_b == 0:
                        break
                    if divide(a, b) != divide(reduced_a, reduced_b):
                        break
                    if a % reduced_a == 0 and b % reduced_b == 0 and a // reduced_a == 10 and b // reduced_b == 10:
                        break
                    digit_cancelling_fractions.append((reduced_a, reduced_b))
    return reduce_fraction(reduce(multiply_fractions, digit_cancelling_fractions))[1]