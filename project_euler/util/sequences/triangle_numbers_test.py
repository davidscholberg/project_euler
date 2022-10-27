from unittest import TestCase

from project_euler.util.iterable.index_cap import index_cap
from project_euler.util.sequences.triangle_numbers import triangle_numbers

class TestTriangleNumbers(TestCase):
    def test_triangle_numbers(self):
        self.assertEqual([1, 3, 6, 10, 15, 21, 28, 36, 45, 55], list(index_cap(triangle_numbers(), 9)))