from unittest import TestCase

from project_euler.util.iterable.sliding_window import sliding_window

class TestSlidingWindow(TestCase):
    def test_sliding_window(self):
        self.assertEqual([6, 9, 12], list(sliding_window(range(1, 6), 3, sum)))
        self.assertEqual([15], list(sliding_window(range(1, 6), 6, sum)))
        self.assertEqual([6, 9, 12], list(sliding_window(range(1, 6), 3, sum, require_full=True)))
        self.assertEqual([], list(sliding_window(range(1, 6), 6, sum, require_full=True)))