from typing import Callable, Iterable

from project_euler.util.grids.grid import Grid

def path_count(grid: Grid, start: tuple[int, int], end: tuple[int, int], moves: Iterable[Callable], grid_cache = None) -> int:
    if grid_cache is None:
        grid_cache = Grid(from_grid=grid, default_value=None)
    if not grid.in_bounds(start):
        return 0
    cached_value = grid_cache.get(start)
    if cached_value is not None:
        return cached_value
    if start == end:
        grid_cache.set(start, 1)
        return 1
    count = sum(map(lambda move: path_count(grid, move(start), end, moves, grid_cache), moves))
    grid_cache.set(start, count)
    return count

def max_path_sum(grid: Grid, start: tuple[int, int], moves: Iterable[Callable], grid_cache: Grid = None) -> int:
    if grid_cache is None:
        grid_cache = Grid(from_grid=grid, default_value=None)
    if not grid_cache.in_bounds(start):
        return 0
    max_sum = grid_cache.get(start)
    if max_sum is not None:
        return max_sum
    child_sums = map(
        lambda move: max_path_sum(grid, move(start), moves, grid_cache=grid_cache),
        moves
    )
    max_sum = max(child_sums) + grid.get(start)
    grid_cache.set(start, max_sum)
    return max_sum