from itertools import starmap
from typing import Iterable, Iterator

def word_score(position: int, word: str) -> int:
    return position * sum(map(
        lambda c: ord(c.upper()) - 64,
        word
    ))

def word_scores(words: Iterable[str]) -> Iterator[int]:
    yield from starmap(
        word_score,
        enumerate(sorted(words), start=1)
    )