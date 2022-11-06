from itertools import chain, count

from project_euler.util.grids.coordinates import move_down_right, move_up_right
from project_euler.util.grids.grid import Grid
from project_euler.util.grids.lines import line
from project_euler.util.grids.spiral import set_spiral

def get_answer() -> int:
    grid = Grid(rows=1001)
    set_spiral(grid, count(start=1))
    down_diagonal = line(grid, grid.top_left(), move_down_right)
    up_diagonal = line(grid, grid.bottom_left(), move_up_right)
    return sum(chain(down_diagonal, up_diagonal)) - 1