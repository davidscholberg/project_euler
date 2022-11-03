from typing import Iterable, Iterator

def word_score(position: int, word: str) -> int:
    return position * sum(map(
        lambda c: ord(c.upper()) - 64,
        word
    ))

def word_scores(words: Iterable[str]) -> Iterator[int]:
    yield from map(
        lambda t: word_score(t[0], t[1]),
        enumerate(sorted(words), start=1)
    )