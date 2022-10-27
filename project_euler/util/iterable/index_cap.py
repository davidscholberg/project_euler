from typing import Iterable, Iterator

def index_cap(iterable: Iterable, cap: int) -> Iterator:
    for i, value in enumerate(iterable):
        if i > cap:
            return
        yield value