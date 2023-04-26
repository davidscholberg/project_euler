from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.sequences.hexagonal_numbers import hexagonal_numbers

class TestHexagonalNumbers(TestCase):
    def test_hexagonal_numbers(self):
        self.assertEqual([1, 6, 15, 28, 45, 66, 91, 120, 153, 190], list(count_cap(10, hexagonal_numbers())))