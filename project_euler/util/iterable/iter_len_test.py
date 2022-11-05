from unittest import TestCase

from project_euler.util.iterable.iter_len import iter_len

class TestIterLen(TestCase):
    def test_iter_len(self):
        self.assertEqual(0, iter_len(range(1, 1)))
        self.assertEqual(1, iter_len(range(1, 2)))
        self.assertEqual(2, iter_len(range(1, 3)))