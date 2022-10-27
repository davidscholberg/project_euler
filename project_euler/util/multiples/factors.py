import math
from typing import Iterator

def factors(n: int, proper: bool = False) -> Iterator[int]:
    yield 1
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            yield i
            partner = n // i
            if partner != i:
                yield partner
    if not proper and n > 1:
        yield n