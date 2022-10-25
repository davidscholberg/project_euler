from typing import Iterator

def split_number(n: int, ways: int = 2, ascending: bool = False, start: int = 1) -> Iterator[tuple]:
    if ways == 1:
        yield (n,)
        return
    next_start = start
    for i in range(start, (n // ways) + 1):
        if ascending:
            next_start = i + 1
            if n - i <= i:
                break
        for sub_result in split_number(n - i, ways - 1, ascending=ascending, start=next_start):
            result = [i]
            result.extend(sub_result)
            yield tuple(result)