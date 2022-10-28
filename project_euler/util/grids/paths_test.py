from unittest import TestCase

from project_euler.util.grids.coordinates import move_down, move_right
from project_euler.util.grids.grid import Grid
from project_euler.util.grids.paths import path_count

class TestPaths(TestCase):
    def test_path_count(self):
        grid = Grid(rows=2)
        self.assertEqual(2, path_count(grid, grid.top_left(), grid.bottom_right(), (move_right, move_down)))
        grid = Grid(rows=3)
        self.assertEqual(6, path_count(grid, grid.top_left(), grid.bottom_right(), (move_right, move_down)))