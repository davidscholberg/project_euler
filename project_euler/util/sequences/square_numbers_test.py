from unittest import TestCase

from project_euler.util.sequences.square_numbers import is_square_number

class TestSquareNumbers(TestCase):
    def test_is_square_number(self):
        self.assertTrue(is_square_number(1))
        self.assertTrue(is_square_number(4))
        self.assertTrue(is_square_number(9))
        self.assertTrue(is_square_number(16))
        self.assertTrue(is_square_number(25))
        self.assertFalse(is_square_number(2))
        self.assertFalse(is_square_number(5))
        self.assertFalse(is_square_number(20))