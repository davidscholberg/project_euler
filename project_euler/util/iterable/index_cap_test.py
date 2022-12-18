from unittest import TestCase

from project_euler.util.iterable.index_cap import index_cap

class TestIndexCap(TestCase):
    def test_index_cap(self):
        self.assertEqual([1, 2, 3, 4], list(index_cap(3, range(1, 6))))
        self.assertEqual([1, 2, 3, 4, 5], list(index_cap(4, range(1, 6))))
        self.assertEqual([1, 2, 3, 4, 5], list(index_cap(5, range(1, 6))))
        self.assertEqual([1, 2, 3, 4], list(index_cap(4, range(1, 6), start=1)))
        self.assertEqual([1, 2, 3, 4, 5], list(index_cap(5, range(1, 6), start=1)))
        self.assertEqual([1, 2, 3, 4, 5], list(index_cap(6, range(1, 6), start=1)))