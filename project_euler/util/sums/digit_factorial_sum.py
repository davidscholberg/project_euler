from project_euler.util.digits.digits import digits

digit_factorial_map = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
"""Map of the factorials of each base-10 digit."""

def digit_factorial_sum(n: int) -> int:
    """Sum of the factorial of each digit of n."""
    total = 0
    for digit in digits(n):
        total += digit_factorial_map[digit]
    return total