from project_euler.util.fractions.reduce import reduce_fraction

def add_fractions(a: tuple[int, int], b: tuple[int, int], reduce: bool = True) -> tuple[int, int]:
    """
    Adds two fractions together, returning the result as a fraction. The result
    may optionally be reduced.
    """
    (numerator_a, denominator_a) = a
    (numerator_b, denominator_b) = b
    result = (
        (numerator_a * denominator_b) + (numerator_b * denominator_a),
        denominator_a * denominator_b
    )
    if reduce:
        return reduce_fraction(result)
    return result