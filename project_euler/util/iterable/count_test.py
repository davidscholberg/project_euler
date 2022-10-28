from unittest import TestCase

from project_euler.util.iterable.count import count

class TestCount(TestCase):
    def test_count(self):
        self.assertEqual(0, count(range(1, 1)))
        self.assertEqual(1, count(range(1, 2)))
        self.assertEqual(2, count(range(1, 3)))