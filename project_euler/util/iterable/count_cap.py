from typing import Iterable, Iterator

from project_euler.util.iterable.index_cap import index_cap

def count_cap(cap: int, iterable: Iterable) -> Iterator:
    return index_cap(cap, iterable, start=1)