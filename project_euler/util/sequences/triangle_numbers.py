from typing import Iterator

def triangle_numbers() -> Iterator[int]:
    index = 1
    current = 1
    while True:
        yield current
        index += 1
        current += index