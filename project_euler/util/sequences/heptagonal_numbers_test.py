from unittest import TestCase

from project_euler.util.sequences.heptagonal_numbers import is_heptagonal_number

class TestHeptagonalNumbers(TestCase):
    def test_is_heptagonal_number(self):
        self.assertTrue(is_heptagonal_number(1))
        self.assertTrue(is_heptagonal_number(7))
        self.assertTrue(is_heptagonal_number(18))
        self.assertTrue(is_heptagonal_number(34))
        self.assertTrue(is_heptagonal_number(55))
        self.assertFalse(is_heptagonal_number(2))
        self.assertFalse(is_heptagonal_number(14))
        self.assertFalse(is_heptagonal_number(49))