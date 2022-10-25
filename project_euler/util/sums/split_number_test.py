from unittest import TestCase

from project_euler.util.sums.split_number import split_number

class TestSplitNumber(TestCase):
    def test_split_number(self):
        self.assertEqual(
            [
                (4,)
            ],
            list(split_number(4, ways=1))
        )
        self.assertEqual(
            [
                (1, 3),
                (2, 2)
            ],
            list(split_number(4, ways=2))
        )
        self.assertEqual(
            [
                (1, 1, 2),
            ],
            list(split_number(4, ways=3))
        )
        self.assertEqual(
            [
                (1, 1, 1, 1),
            ],
            list(split_number(4, ways=4))
        )
        self.assertEqual(
            [],
            list(split_number(4, ways=5))
        )
        self.assertEqual(
            [
                (5,)
            ],
            list(split_number(5, ways=1))
        )
        self.assertEqual(
            [
                (1, 4),
                (2, 3)
            ],
            list(split_number(5, ways=2))
        )
        self.assertEqual(
            [
                (1, 1, 3),
                (1, 2, 2),
            ],
            list(split_number(5, ways=3))
        )
        self.assertEqual(
            [
                (1, 1, 1, 2),
            ],
            list(split_number(5, ways=4))
        )
        self.assertEqual(
            [
                (1, 1, 1, 1, 1),
            ],
            list(split_number(5, ways=5))
        )
        self.assertEqual(
            [],
            list(split_number(5, ways=6))
        )
        self.assertEqual(
            [
                (4,)
            ],
            list(split_number(4, ways=1, ascending=True))
        )
        self.assertEqual(
            [
                (1, 3)
            ],
            list(split_number(4, ways=2, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(4, ways=3, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(4, ways=4, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(4, ways=5, ascending=True))
        )
        self.assertEqual(
            [
                (5,)
            ],
            list(split_number(5, ways=1, ascending=True))
        )
        self.assertEqual(
            [
                (1, 4),
                (2, 3)
            ],
            list(split_number(5, ways=2, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(5, ways=3, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(5, ways=4, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(5, ways=5, ascending=True))
        )
        self.assertEqual(
            [],
            list(split_number(5, ways=6, ascending=True))
        )