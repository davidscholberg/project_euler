from itertools import chain
from typing import Iterable, Iterator

def sum_combinations(n: int, parts: Iterable[int]) -> Iterator[Iterator[int]]:
    if n == 0:
        return
    parts_list = list(parts)
    if len(parts_list) == 0:
        return
    part = parts_list[-1]
    difference = n - part
    if difference == 0:
        yield iter((part,))
    elif difference > 0:
        for subcombination in sum_combinations(difference, parts_list):
            yield chain((part,), subcombination)
    if len(parts_list) == 1:
        return
    parts_list.pop()
    yield from sum_combinations(n, parts_list)