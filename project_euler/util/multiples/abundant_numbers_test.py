from unittest import TestCase

from project_euler.util.multiples.abundant_numbers import abundant_numbers, numbers_not_sum_of_two_abundant_numbers

class TestAbundantNumbers(TestCase):
    def test_abundant_numbers(self):
        self.assertEqual(
            (12, 18, 20, 24, 30, 36, 40, 42, 48, 54),
            tuple(abundant_numbers(12, 54))
        )

    def test_numbers_not_sum_of_two_abundant_numbers(self):
        self.assertEqual(
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 33, 34, 35, 37, 39),
            tuple(numbers_not_sum_of_two_abundant_numbers(40))
        )