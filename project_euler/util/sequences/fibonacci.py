from typing import Iterator

def fibonacci() -> Iterator[int]:
    yield 1
    yield 1
    previous = 1
    current = 1
    while True:
        next = previous + current
        yield next
        previous = current
        current = next