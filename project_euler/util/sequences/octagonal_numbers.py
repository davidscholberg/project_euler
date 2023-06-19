def is_octagonal_number(n: int) -> bool:
    """Tells if n is an octagonal number."""
    return (((((3 * n) + 1) ** 0.5) + 1) / 3).is_integer()