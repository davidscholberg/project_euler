from unittest import TestCase

from project_euler.util.grids.coordinates import move_down, move_down_right, move_right
from project_euler.util.grids.grid import Grid
from project_euler.util.iterable.count import count
from project_euler.util.grids.paths import max_path_sum, path_count

class TestPaths(TestCase):
    def test_path_count(self):
        grid = Grid(rows=2)
        self.assertEqual(2, path_count(grid, grid.top_left(), grid.bottom_right(), (move_right, move_down)))
        grid = Grid(rows=3)
        self.assertEqual(6, path_count(grid, grid.top_left(), grid.bottom_right(), (move_right, move_down)))

    def test_max_path_sum(self):
        grid_data = (
            "02\n"
            "12 53\n"
            "60 50 32\n"
        )
        grid = Grid(grid_data=grid_data)
        self.assertEqual(105, max_path_sum(grid, grid.top_left(), (move_down, move_down_right)))