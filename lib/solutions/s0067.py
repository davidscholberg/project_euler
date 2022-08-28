from ..util.grids import Grid, TriangleGridSum
from ..util.project_paths import get_data_file_path

def get_answer() -> int:
    triangle_grid_sum = TriangleGridSum(get_data_file_path("triangle_grid_100_rows.txt"))
    return triangle_grid_sum.get_max_sum_from_coordinates_to_bounds((0, 0), (Grid.move_down, Grid.move_down_right))