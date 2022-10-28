from project_euler.util.grids.coordinates import move_down, move_right
from project_euler.util.grids.grid import Grid
from project_euler.util.grids.paths import path_count

def get_answer() -> int:
    grid = Grid(rows=21)
    return path_count(grid, grid.top_left(), grid.bottom_right(), (move_right, move_down))