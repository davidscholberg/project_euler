from typing import Iterable, Iterator

def value_cap(iterable: Iterable, cap) -> Iterator:
    iterator = iter(iterable)
    while True:
        try:
            current_value = next(iterator)
        except StopIteration:
            return
        if current_value > cap:
            return
        yield current_value