from ..util.decimals import divide

def get_answer() -> int:
    divisor_with_most_repeating_digits = 0
    max_repeating_digits = 0
    for i in range(1, 1000):
        quotient = divide(1, i)
        if len(quotient.repeating_digits) > max_repeating_digits:
            max_repeating_digits = len(quotient.repeating_digits)
            divisor_with_most_repeating_digits = i
    return divisor_with_most_repeating_digits