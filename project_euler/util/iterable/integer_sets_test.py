from unittest import TestCase

from project_euler.util.iterable.integer_sets import integer_pairs

class TestIntegerSets(TestCase):
    def test_integer_pairs(self):
        self.assertEqual(
            [
                (1, 2)
            ],
            list(integer_pairs(1, 2, distinct=True))
        )
        self.assertEqual(
            [
                (1, 2),
                (1, 3),
                (2, 3)
            ],
            list(integer_pairs(1, 3, distinct=True))
        )
        self.assertEqual(
            [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 3),
                (2, 4),
                (3, 4)
            ],
            list(integer_pairs(1, 4, distinct=True))
        )
        self.assertEqual(
            [
                (1, 1),
                (1, 2),
                (2, 2)
            ],
            list(integer_pairs(1, 2, distinct=False))
        )
        self.assertEqual(
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (2, 2),
                (2, 3),
                (3, 3)
            ],
            list(integer_pairs(1, 3, distinct=False))
        )
        self.assertEqual(
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 2),
                (2, 3),
                (2, 4),
                (3, 3),
                (3, 4),
                (4, 4)
            ],
            list(integer_pairs(1, 4, distinct=False))
        )