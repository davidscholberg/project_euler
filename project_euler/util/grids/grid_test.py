from unittest import TestCase

from project_euler.util.grids.grid import Grid

class TestGrid(TestCase):
    def test_grid(self):
        grid_data = (
            "02 04\n"
            "12 53 19\n"
            "60 50 32\n"
        )
        grid = Grid(grid_data=grid_data)
        self.assertEqual(2, grid.get(grid.top_left()))
        self.assertEqual(60, grid.get(grid.bottom_left()))
        self.assertEqual(4, grid.get(grid.top_right()))
        self.assertEqual(32, grid.get(grid.bottom_right()))
        grid.set((1, 1), 94)
        self.assertEqual(94, grid.get((1, 1)))
        self.assertTrue(grid.in_bounds((2, 2)))
        self.assertFalse(grid.in_bounds((2, 3)))
        self.assertFalse(grid.in_bounds((3, 2)))
        self.assertFalse(grid.in_bounds((3, 3)))
        self.assertFalse(grid.in_bounds((0, 2)))
        self.assertTrue(grid.is_on_top_edge((0, 1)))
        self.assertTrue(grid.is_on_right_edge((0, 1)))
        self.assertTrue(grid.is_on_left_edge((1, 0)))
        self.assertTrue(grid.is_on_bottom_edge((2, 1)))
        self.assertFalse(grid.is_on_top_edge((0, 2)))
        grid = Grid(rows=3, default_value=10)
        self.assertEqual(10, grid.get(grid.top_left()))
        self.assertEqual(10, grid.get(grid.bottom_left()))
        self.assertEqual(10, grid.get(grid.top_right()))
        self.assertEqual(10, grid.get(grid.bottom_right()))
        grid.set((1, 1), 94)
        self.assertEqual(94, grid.get((1, 1)))
        self.assertTrue(grid.in_bounds((2, 2)))
        self.assertFalse(grid.in_bounds((2, 3)))
        self.assertFalse(grid.in_bounds((3, 2)))
        self.assertFalse(grid.in_bounds((3, 3)))
        from_grid = Grid(from_grid=grid)
        self.assertEqual(0, from_grid.get(from_grid.top_left()))
        self.assertEqual(0, from_grid.get(from_grid.bottom_left()))
        self.assertEqual(0, from_grid.get(from_grid.top_right()))
        self.assertEqual(0, from_grid.get(from_grid.bottom_right()))
        self.assertTrue(from_grid.in_bounds((2, 2)))
        self.assertFalse(from_grid.in_bounds((3, 3)))
        grid1 = Grid(grid_data=grid_data)
        grid2 = Grid(grid_data=grid_data)
        self.assertEqual(grid1, grid2)
        grid2 = Grid(rows=3, default_value=10)
        self.assertNotEqual(grid1, grid2)