from unittest import TestCase

from project_euler.util.grids.coordinates import move_down, move_right
from project_euler.util.grids.grid import Grid
from project_euler.util.grids.lines import line, lines, lines_down_diagonal, lines_horizontal, lines_up_diagonal, lines_vertical

class TestLines(TestCase):
    def test_line(self):
        grid_data = (
            "02 04 21\n"
            "12 53 19\n"
            "60 50 32\n"
        )
        grid = Grid(grid_data=grid_data)
        self.assertEqual([2, 12, 60], list(line(grid, grid.top_left(), move_down)))

    def test_lines(self):
        grid_data = (
            "02 04 21\n"
            "12 53 19\n"
            "60 50 32\n"
        )
        grid = Grid(grid_data=grid_data)
        self.assertEqual(
            [
                [2, 12, 60],
                [4, 53, 50],
                [21, 19, 32],
            ],
            list(map(list, lines(grid, grid.top_left(), move_down, move_right)))
        )
        self.assertEqual(
            [
                [2, 12, 60],
                [4, 53, 50],
                [21, 19, 32],
            ],
            list(map(list, lines_vertical(grid)))
        )
        self.assertEqual(
            [
                [2, 4, 21],
                [12, 53, 19],
                [60, 50, 32],
            ],
            list(map(list, lines_horizontal(grid)))
        )
        self.assertEqual(
            [
                [2],
                [12, 4],
                [60, 53, 21],
                [50, 19],
                [32]
            ],
            list(map(list, lines_up_diagonal(grid)))
        )
        self.assertEqual(
            [
                [60],
                [12, 50],
                [2, 53, 32],
                [4, 19],
                [21]
            ],
            list(map(list, lines_down_diagonal(grid)))
        )