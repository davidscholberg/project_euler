from project_euler.paths import data_file_path
from project_euler.util.grids.coordinates import move_down, move_down_right
from project_euler.util.grids.grid import Grid
from project_euler.util.grids.paths import max_path_sum

def get_answer() -> int:
    with open(data_file_path('15_row_triangle_grid.txt')) as file:
        grid = Grid(grid_data=file.read())
        return max_path_sum(grid, grid.top_left(), (move_down, move_down_right))