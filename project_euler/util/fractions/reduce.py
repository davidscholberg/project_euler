from project_euler.util.fractions.greatest_common_divisor import greatest_common_divisor

def reduce_fraction(fraction: tuple[int, int]) -> tuple[int, int]:
    """Reduce the given fraction to the lowest integer values."""
    (numerator, denominator) = fraction
    if denominator == 1:
        return fraction
    if numerator == denominator:
        return (1, 1)
    gcd = greatest_common_divisor(fraction)
    return (numerator // gcd, denominator // gcd)