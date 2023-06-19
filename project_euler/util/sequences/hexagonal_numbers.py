from typing import Iterator

def hexagonal_numbers() -> Iterator[int]:
    current = 1
    difference = 5
    while True:
        yield current
        current += difference
        difference += 4

def is_hexagonal_number(n: int) -> bool:
    """Tells if n is a hexagonal number."""
    return (((((8 * n) + 1) ** 0.5) + 1) / 4).is_integer()