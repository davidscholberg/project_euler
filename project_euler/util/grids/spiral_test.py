from itertools import count
from unittest import TestCase

from project_euler.util.grids.grid import Grid
from project_euler.util.grids.spiral import set_spiral

class TestSpiral(TestCase):
    def test_set_spiral(self):
        spiral_grid_data = (
            "21 22 23 24 25\n"
            "20 07 08 09 10\n"
            "19 06 01 02 11\n"
            "18 05 04 03 12\n"
            "17 16 15 14 13\n"
        )
        grid = Grid(rows=5)
        set_spiral(grid, count(start=1))
        self.assertEqual(Grid(grid_data=spiral_grid_data), grid)