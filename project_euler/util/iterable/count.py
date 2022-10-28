from typing import Iterator

def count(iterator: Iterator) -> int:
    item_count = 0
    for _ in iterator:
        item_count += 1
    return item_count