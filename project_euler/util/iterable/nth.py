from typing import Any, Iterator

def nth(n: int, iterator: Iterator[Any]) -> Any:
    for i, value in enumerate(iterator, start=1):
        if i == n:
            return value
    raise IndexError()