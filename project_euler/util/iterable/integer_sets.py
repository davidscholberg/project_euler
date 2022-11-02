from typing import Iterator

def integer_pairs(minimum: int, maximum: int, distinct: bool) -> Iterator[tuple[int, int]]:
    distinct_min_offset = 0
    distinct_max_offset = 1
    if distinct:
        distinct_min_offset = 1
        distinct_max_offset = 0
    for i in range(minimum, maximum + distinct_max_offset):
        for j in range(i + distinct_min_offset, maximum + 1):
            yield (i, j)