from typing import Iterable, Iterator

from project_euler.util.iterable.index_cap import index_cap

def count_cap(iterable: Iterable, cap: int) -> Iterator:
    return index_cap(iterable, cap, start=1)