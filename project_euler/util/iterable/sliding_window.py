from collections import deque
from typing import Any, Callable, Iterable, Iterator

def sliding_window(iterable: Iterable, window_size: int, operation: Callable[[Iterator], Any]) -> Iterator:
    iterator = iter(iterable)
    window = deque(maxlen=window_size)
    for _ in range(0, window_size):
        try:
            window.append(next(iterator))
        except StopIteration:
            break
    while True:
        yield operation(iter(window))
        try:
            window.append(next(iterator))
        except StopIteration:
            break