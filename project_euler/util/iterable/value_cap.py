from typing import Iterable, Iterator

def value_cap(iterable: Iterable, cap) -> Iterator:
    for value in iterable:
        if value > cap:
            return
        yield value