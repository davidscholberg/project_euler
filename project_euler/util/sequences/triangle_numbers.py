from typing import Iterator

def is_triangle_number(n: int) -> bool:
    return (((8 * n) + 1) ** 0.5).is_integer()

def triangle_number(nth: int) -> int:
    return (nth * (nth + 1)) // 2

def triangle_numbers() -> Iterator[int]:
    index = 1
    current = 1
    while True:
        yield current
        index += 1
        current += index