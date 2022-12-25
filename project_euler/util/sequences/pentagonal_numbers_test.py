from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.sequences.pentagonal_numbers import pentagonal_numbers, is_pentagonal_number

class TestPentagonalNumbers(TestCase):
    def test_pentagonal_numbers(self):
        self.assertEqual(
            (1, 5, 12, 22, 35, 51, 70, 92, 117, 145),
            tuple(count_cap(10, pentagonal_numbers()))
        )

    def test_is_pentagonal_number(self):
        self.assertTrue(is_pentagonal_number(1))
        self.assertTrue(is_pentagonal_number(5))
        self.assertTrue(is_pentagonal_number(22))
        self.assertTrue(is_pentagonal_number(70))
        self.assertTrue(is_pentagonal_number(145))
        self.assertFalse(is_pentagonal_number(2))
        self.assertFalse(is_pentagonal_number(3))
        self.assertFalse(is_pentagonal_number(4))
        self.assertFalse(is_pentagonal_number(56))
        self.assertFalse(is_pentagonal_number(97))