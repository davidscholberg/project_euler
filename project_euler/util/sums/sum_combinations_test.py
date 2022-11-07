from unittest import TestCase

from project_euler.util.sums.sum_combinations import sum_combinations

class TestSumCombinations(TestCase):
    def test_sum_combinations(self):
        self.assertEqual(
            (
                (2, 2, 1),
                (2, 1, 1, 1),
                (1, 1, 1, 1, 1)
            ),
            tuple(map(tuple, sum_combinations(5, (1, 2))))
        )
        self.assertEqual(
            (
                (3, 2),
                (3, 1, 1),
                (2, 2, 1),
                (2, 1, 1, 1),
                (1, 1, 1, 1, 1),
            ),
            tuple(map(tuple, sum_combinations(5, (1, 2, 3))))
        )