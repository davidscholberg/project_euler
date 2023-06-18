from project_euler.util.digits.digits import digit_count

def concatenate_integers(a: int, b: int) -> int:
    """Concatenate integer a at the beginning of b."""
    return (a * (10 ** digit_count(b))) + b