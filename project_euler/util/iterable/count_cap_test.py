from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap

class TestCountCap(TestCase):
    def test_count_cap(self):
        self.assertEqual([1, 2, 3, 4], list(count_cap(4, range(1, 6))))
        self.assertEqual([1, 2, 3, 4, 5], list(count_cap(5, range(1, 6))))
        self.assertEqual([1, 2, 3, 4, 5], list(count_cap(6, range(1, 6))))