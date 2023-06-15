from unittest import TestCase

from project_euler.util.fractions.add import add_fractions

class TestAdd(TestCase):
    def test_add_fractions(self):
        self.assertEqual(add_fractions((1, 2), (7, 8)), (11, 8))
        self.assertEqual(add_fractions((1, 2), (6, 8)), (5, 4))
        self.assertEqual(add_fractions((4, 3), (7, 8)), (53, 24))
        self.assertEqual(add_fractions((4, 3), (9, 8)), (59, 24))
        self.assertEqual(add_fractions((1, 2), (7, 8), reduce=False), (22, 16))
        self.assertEqual(add_fractions((1, 2), (6, 8), reduce=False), (20, 16))
        self.assertEqual(add_fractions((4, 3), (7, 8), reduce=False), (53, 24))
        self.assertEqual(add_fractions((4, 3), (9, 8), reduce=False), (59, 24))