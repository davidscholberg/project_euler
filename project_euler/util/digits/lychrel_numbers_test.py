from unittest import TestCase

from project_euler.util.digits.lychrel_numbers import is_lychrel_number

class TestLychrelNumbers(TestCase):
    def test_is_lychrel_number(self):
        self.assertFalse(is_lychrel_number(47))
        self.assertFalse(is_lychrel_number(349))
        self.assertTrue(is_lychrel_number(196))
        non_lychrel_cache = set()
        self.assertFalse(is_lychrel_number(349, non_lychrel_cache))
        self.assertEqual(non_lychrel_cache, set((349, 943, 1292, 2921, 4213, 3124)))