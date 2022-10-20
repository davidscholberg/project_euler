from typing import Iterator

def multiples(n: int) -> Iterator[int]:
    current_multiple = n
    while True:
        yield current_multiple
        current_multiple += n