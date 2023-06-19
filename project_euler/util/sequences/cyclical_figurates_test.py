from unittest import TestCase

from project_euler.util.sequences.cyclical_figurates import cyclical_figurates
from project_euler.util.sequences.pentagonal_numbers import is_pentagonal_number
from project_euler.util.sequences.square_numbers import is_square_number
from project_euler.util.sequences.triangle_numbers import is_triangle_number

class TestCyclicalFigurates(TestCase):
    def test_cyclical_figurates(self):
        figurate_tests = (
            is_triangle_number,
            is_square_number,
            is_pentagonal_number
        )
        self.assertEqual(cyclical_figurates(figurate_tests), (2882, 8281, 8128))