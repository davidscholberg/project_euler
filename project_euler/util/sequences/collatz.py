from typing import Iterator

def collatz(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return (3 * n) + 1

def collatz_sequence(n: int) -> Iterator[int]:
    current = n
    while True:
        yield current
        if current == 1:
            return
        current = collatz(current)

class Collatz:
    def __init__(self) -> None:
        self._cache = {}
        self._cache[1] = 1

    def sequence_length(self, n: int) -> int:
        if n in self._cache:
            return self._cache[n]
        length = 1 + self.sequence_length(collatz(n))
        self._cache[n] = length
        return length