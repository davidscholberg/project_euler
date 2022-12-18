from typing import Iterable, Iterator

def index_cap(cap: int, iterable: Iterable, start: int = 0) -> Iterator:
    for i, value in enumerate(iterable, start=start):
        if i > cap:
            return
        yield value