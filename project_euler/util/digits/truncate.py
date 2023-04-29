from project_euler.util.digits.digits import digit_count

def left_truncate(n: int, to: int = 1):
    """Truncate leftmost digits of n to "to" digits."""
    if n < 10 ** to:
        return n
    number_of_digits = digit_count(n)
    current_n = n
    for i in range(number_of_digits - to):
        current_digit_count = number_of_digits - i
        leftmost_digit = current_n // (10 ** (current_digit_count - 1))
        current_n -= (leftmost_digit * (10 ** (current_digit_count - 1)))
    return current_n


def right_truncate(n: int) -> int:
    """Truncate the rightmost digit of given integer. Raise ValueError if n < 10."""
    if n < 10:
        raise ValueError("right_truncate: n must have more than 1 digit")
    return n // 10