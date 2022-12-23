from typing import Iterable, Iterator

def value_cap(cap, iterable: Iterable) -> Iterator:
    for value in iterable:
        if value > cap:
            return
        yield value