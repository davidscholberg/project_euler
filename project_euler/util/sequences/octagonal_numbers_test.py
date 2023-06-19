from unittest import TestCase

from project_euler.util.sequences.octagonal_numbers import is_octagonal_number

class TestOctagonalNumbers(TestCase):
    def test_is_octagonal_number(self):
        self.assertTrue(is_octagonal_number(1))
        self.assertTrue(is_octagonal_number(8))
        self.assertTrue(is_octagonal_number(21))
        self.assertTrue(is_octagonal_number(40))
        self.assertTrue(is_octagonal_number(65))
        self.assertFalse(is_octagonal_number(2))
        self.assertFalse(is_octagonal_number(16))
        self.assertFalse(is_octagonal_number(64))