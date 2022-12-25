from typing import Iterator

def pentagonal_numbers() -> Iterator[int]:
    current_value = 1
    difference = 4
    while True:
        yield current_value
        current_value += difference
        difference += 3