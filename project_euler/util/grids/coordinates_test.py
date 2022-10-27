from unittest import TestCase

from project_euler.util.grids import coordinates

class TestCoordinates(TestCase):
    def test_move(self):
        self.assertEqual((-1, 0), coordinates.move_up((0, 0)))
        self.assertEqual((-2, 0), coordinates.move_up((0, 0), step=2))
        self.assertEqual((1, 0), coordinates.move_down((0, 0)))
        self.assertEqual((2, 0), coordinates.move_down((0, 0), step=2))
        self.assertEqual((0, -1), coordinates.move_left((0, 0)))
        self.assertEqual((0, -2), coordinates.move_left((0, 0), step=2))
        self.assertEqual((0, 1), coordinates.move_right((0, 0)))
        self.assertEqual((0, 2), coordinates.move_right((0, 0), step=2))
        self.assertEqual((-1, -1), coordinates.move_up_left((0, 0)))
        self.assertEqual((-2, -2), coordinates.move_up_left((0, 0), step=2))
        self.assertEqual((-1, 1), coordinates.move_up_right((0, 0)))
        self.assertEqual((-2, 2), coordinates.move_up_right((0, 0), step=2))
        self.assertEqual((1, -1), coordinates.move_down_left((0, 0)))
        self.assertEqual((2, -2), coordinates.move_down_left((0, 0), step=2))
        self.assertEqual((1, 1), coordinates.move_down_right((0, 0)))
        self.assertEqual((2, 2), coordinates.move_down_right((0, 0), step=2))