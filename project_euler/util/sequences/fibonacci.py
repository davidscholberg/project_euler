from typing import Iterator

def fibonacci() -> Iterator[int]:
    yield 0
    yield 1
    previous = 0
    current = 1
    while True:
        next = previous + current
        yield next
        previous = current
        current = next