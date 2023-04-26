from typing import Iterator

def hexagonal_numbers() -> Iterator[int]:
    current = 1
    difference = 5
    while True:
        yield current
        current += difference
        difference += 4