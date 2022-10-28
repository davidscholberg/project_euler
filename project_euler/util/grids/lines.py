from itertools import chain
from typing import Callable, Iterator

from project_euler.util.grids.coordinates import move_down, move_down_right, move_right, move_up, move_up_right
from project_euler.util.grids.grid import Grid

def line(grid: Grid, start: tuple[int, int], move: Callable) -> Iterator:
    current = start
    while grid.in_bounds(current):
        yield grid.get(current)
        current = move(current)

def lines(grid: Grid, start: tuple[int, int], move: Callable, move_start: Callable) -> Iterator[Iterator]:
    current_start = start
    while grid.in_bounds(current_start):
        yield line(grid, current_start, move)
        current_start = move_start(current_start)

def lines_vertical(grid: Grid) -> Iterator[Iterator]:
    return lines(grid, grid.top_left(), move_down, move_right)

def lines_horizontal(grid: Grid) -> Iterator[Iterator]:
    return lines(grid, grid.top_left(), move_right, move_down)

def lines_up_diagonal(grid: Grid) -> Iterator[Iterator]:
    return chain(
        lines(grid, grid.top_left(), move_up_right, move_down),
        lines(grid, move_right(grid.bottom_left()), move_up_right, move_right)
    )

def lines_down_diagonal(grid: Grid) -> Iterator[Iterator]:
    return chain(
        lines(grid, grid.bottom_left(), move_down_right, move_up),
        lines(grid, move_right(grid.top_left()), move_down_right, move_right)
    )