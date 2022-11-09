from collections import deque
from typing import Any, Iterable, Iterator

def rotations(iterable: Iterable[Any]) -> Iterator[tuple[Any]]:
    """Returns all rotations of a given iterable. E.g. ABC, CAB, BCA"""
    d = deque(iterable)
    yield tuple(d)
    for _ in range(len(d) - 1):
        d.rotate(1)
        yield tuple(d)