def is_heptagonal_number(n: int) -> bool:
    """Tells if n is a heptagonal number."""
    return (((((40 * n) + 9) ** 0.5) + 3) / 10).is_integer()