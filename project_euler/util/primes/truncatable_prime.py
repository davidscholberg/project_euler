from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.primes.is_prime import is_prime

def is_left_truncatable_prime(n: int) -> bool:
    """Removing one digit successively from the left of n yields all primes."""
    if not is_prime(n):
        return False
    digits_tuple = digits(n)
    for i in range(1, len(digits_tuple)):
        if not is_prime(number_from_digits(digits_tuple[i:])):
            return False
    return True

def is_right_truncatable_prime(n: int) -> bool:
    """Removing one digit successively from the right of n yields all primes."""
    if not is_prime(n):
        return False
    digits_tuple = digits(n)
    for i in range(len(digits_tuple) - 1, 0, -1):
        if not is_prime(number_from_digits(digits_tuple[:i])):
            return False
    return True