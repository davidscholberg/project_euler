from typing import Iterator

def triangle_number(nth: int) -> int:
    return (nth * (nth + 1)) // 2

def triangle_numbers() -> Iterator[int]:
    index = 1
    current = 1
    while True:
        yield current
        index += 1
        current += index