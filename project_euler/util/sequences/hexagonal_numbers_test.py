from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.sequences.hexagonal_numbers import hexagonal_numbers, is_hexagonal_number

class TestHexagonalNumbers(TestCase):
    def test_hexagonal_numbers(self):
        self.assertEqual([1, 6, 15, 28, 45, 66, 91, 120, 153, 190], list(count_cap(10, hexagonal_numbers())))

    def test_is_hexagonal_number(self):
        self.assertTrue(is_hexagonal_number(1))
        self.assertTrue(is_hexagonal_number(6))
        self.assertTrue(is_hexagonal_number(15))
        self.assertTrue(is_hexagonal_number(28))
        self.assertTrue(is_hexagonal_number(45))
        self.assertFalse(is_hexagonal_number(2))
        self.assertFalse(is_hexagonal_number(12))
        self.assertFalse(is_hexagonal_number(36))