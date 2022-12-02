def right_truncate(n: int) -> int:
    """Truncate the rightmost digit of given integer. Raise ValueError if n < 10."""
    if n < 10:
        raise ValueError("right_truncate: n must have more than 1 digit")
    return n // 10