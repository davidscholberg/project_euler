from itertools import cycle
from typing import Any, Callable, Iterable, Iterator

from project_euler.util.grids.coordinates import move_down, move_left, move_right, move_up
from project_euler.util.grids.grid import Grid

def set_spiral(grid: Grid, values: Iterable[Any]) -> None:
    def next_move() -> Iterator[Callable]:
        moves = (move_right, move_down, move_left, move_up)
        while True:
            for i, move in enumerate(cycle(moves), start=2):
                for _ in range(i // 2):
                    yield move
    bottom_right = grid.bottom_right()
    center = (bottom_right[0] // 2, bottom_right[1] // 2)
    current = center
    for value, move in zip(values, next_move()):
        if not grid.in_bounds(current):
            break
        grid.set(current, value)
        current = move(current)

def spiral_diagonals(layer: int) -> tuple[int, int, int, int]:
    """
    Returns the set of diagonals at the given layer of a square spiral that
    begins with one. The output is only valid for layers 2 and higher.

    This implementation takes advantage of the fact that the odd squares are the
    final diagonal in a given layer.
    """
    odd_square = ((2 * layer) - 1) ** 2
    gap = 2 * (layer - 1)
    return (odd_square - (gap * 3), odd_square - (gap * 2), odd_square - (gap * 1), odd_square)