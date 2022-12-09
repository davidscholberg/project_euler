from unittest import TestCase

from project_euler.util.sequences.permutations import permutations

class TestPermutations(TestCase):
    def test_permutations(self):
        self.assertEqual(
            (
                (0, 1),
                (1, 0)
            ),
            tuple(permutations(2))
        )
        self.assertEqual(
            (
                (0, 1, 2),
                (0, 2, 1),
                (1, 0, 2),
                (1, 2, 0),
                (2, 0, 1),
                (2, 1, 0)
            ),
            tuple(permutations(3))
        )
        self.assertEqual(
            (
                (0, 1),
                (1, 0),
                (0, 2),
                (2, 0),
                (1, 2),
                (2, 1)
            ),
            tuple(permutations(3, choose=2))
        )