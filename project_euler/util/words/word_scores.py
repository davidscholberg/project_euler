from itertools import starmap
from typing import Iterable, Iterator

def word_score(position: int, word: str) -> int:
    return position * word_value(word)

def word_scores(words: Iterable[str]) -> Iterator[int]:
    yield from starmap(
        word_score,
        enumerate(sorted(words), start=1)
    )

def word_value(word: str) -> int:
    return sum(map(
        lambda c: ord(c.upper()) - 64,
        word
    ))