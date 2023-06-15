def greatest_common_divisor(fraction: tuple[int, int]) -> int:
    """Returns the greatest common divisor of the given fraction."""
    bigger = max(fraction)
    smaller = min(fraction)
    remainder = bigger % smaller
    while remainder != 0:
        bigger = smaller
        smaller = remainder
        remainder = bigger % smaller
    return smaller