from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.sequences.pentagonal_numbers import pentagonal_numbers

class TestPentagonalNumbers(TestCase):
    def test_pentagonal_numbers(self):
        self.assertEqual(
            (1, 5, 12, 22, 35, 51, 70, 92, 117, 145),
            tuple(count_cap(10, pentagonal_numbers()))
        )