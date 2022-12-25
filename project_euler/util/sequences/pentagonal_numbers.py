from typing import Iterator

def pentagonal_numbers() -> Iterator[int]:
    current_value = 1
    difference = 4
    while True:
        yield current_value
        current_value += difference
        difference += 3

def is_pentagonal_number(n: int) -> bool:
    return (((((24 * n) + 1) ** 0.5) + 1) / 6).is_integer()