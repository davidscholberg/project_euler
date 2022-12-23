from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.sequences.triangle_numbers import triangle_number, triangle_numbers

class TestTriangleNumbers(TestCase):
    def test_triangle_number(self):
        self.assertEqual(1, triangle_number(1))
        self.assertEqual(3, triangle_number(2))
        self.assertEqual(6, triangle_number(3))
        self.assertEqual(36, triangle_number(8))
        self.assertEqual(45, triangle_number(9))
        self.assertEqual(55, triangle_number(10))

    def test_triangle_numbers(self):
        self.assertEqual([1, 3, 6, 10, 15, 21, 28, 36, 45, 55], list(count_cap(10, triangle_numbers())))