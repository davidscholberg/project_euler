from itertools import starmap
from typing import Any, Iterable, Iterator

def polynomial(coefficients: Iterable[Any], inputs: Iterable[Any]) -> Iterator[Any]:
    for x in inputs:
        yield sum(starmap(
            lambda power, coefficient: coefficient * (x ** power),
            enumerate(reversed(coefficients))
        ))