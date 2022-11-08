from itertools import chain
from typing import Any, Iterable, Iterator

def permutations(iterable: Iterable[Any], choose: int | None = None) -> Iterator[Iterator[Any]]:
    t = tuple(iterable)
    if choose is None:
        choose = len(t)
    if len(t) == 0 or choose == 0:
        yield iter(())
        return
    if choose == 1:
        for i in range(0, len(t)):
            yield iter((t[i],))
        return
    for i in range(0, len(t)):
        sublist = list(t)
        constant = sublist.pop(i)
        for subpermutation in permutations(sublist, choose=choose - 1):
            yield chain((constant,), subpermutation)