from unittest import TestCase

from project_euler.util.iterable.index_cap import index_cap

class TestIndexCap(TestCase):
    def test_index_cap(self):
        self.assertEqual([1, 2, 3, 4], list(index_cap(range(1, 6), 3)))
        self.assertEqual([1, 2, 3, 4, 5], list(index_cap(range(1, 6), 4)))
        self.assertEqual([1, 2, 3, 4, 5], list(index_cap(range(1, 6), 5)))