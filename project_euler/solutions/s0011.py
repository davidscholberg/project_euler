from itertools import chain
from math import prod

from project_euler.paths import data_file_path
from project_euler.util.grids.grid import Grid
from project_euler.util.grids.iterators import lines_down_diagonal, lines_horizontal, lines_up_diagonal, lines_vertical
from project_euler.util.iterable.sliding_window import sliding_window

def get_answer() -> int:
    with open(data_file_path('20x20_grid.txt')) as file:
        grid = Grid(grid_data=file.read())
        grid_lines = chain(
            lines_vertical(grid),
            lines_horizontal(grid),
            lines_up_diagonal(grid),
            lines_down_diagonal(grid)
        )
        sliding_windows = map(lambda grid_line: sliding_window(grid_line, 4, prod, require_full=True), grid_lines)
        return max(chain.from_iterable(sliding_windows))