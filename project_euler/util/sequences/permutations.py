from itertools import chain
from typing import Any, Iterable, Iterator

def permutations(iterable: Iterable[Any]) -> Iterator[Iterator[Any]]:
    t = tuple(iterable)
    if len(t) == 0:
        yield ()
        return
    for i in range(0, len(t)):
        sublist = list(t)
        constant = sublist.pop(i)
        for subpermutation in permutations(sublist):
            yield chain((constant,), subpermutation)