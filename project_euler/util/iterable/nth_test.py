from unittest import TestCase

from project_euler.util.iterable.nth import nth

class TestNth(TestCase):
    def test_nth(self):
        self.assertEqual(2, nth(2, range(1, 4)))
        self.assertEqual(3, nth(3, range(1, 4)))
        self.assertRaises(IndexError, lambda: nth(4, range(1, 4)))