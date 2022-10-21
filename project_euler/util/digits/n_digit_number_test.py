from unittest import TestCase

from project_euler.util.digits.n_digit_number import max_n_digit_number, min_n_digit_number, unique_pairs_of_n_digit_numbers

class TestNDigitNumber(TestCase):
    def test_max_n_digit_number(self):
        self.assertEqual(9, max_n_digit_number(1))
        self.assertEqual(99, max_n_digit_number(2))
        self.assertEqual(999, max_n_digit_number(3))
        self.assertEqual(9999, max_n_digit_number(4))
        self.assertEqual(99999, max_n_digit_number(5))

    def test_min_n_digit_number(self):
        self.assertEqual(0, min_n_digit_number(1))
        self.assertEqual(10, min_n_digit_number(2))
        self.assertEqual(100, min_n_digit_number(3))
        self.assertEqual(1000, min_n_digit_number(4))
        self.assertEqual(10000, min_n_digit_number(5))

    def test_unique_pairs_of_n_digit_numbers(self):
        self.assertEqual(
            [
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (0, 7),
                (0, 8),
                (0, 9),
                (1, 2),
                (1, 3),
                (1, 4),
                (1, 5),
                (1, 6),
                (1, 7),
                (1, 8),
                (1, 9),
                (2, 3),
                (2, 4),
                (2, 5),
                (2, 6),
                (2, 7),
                (2, 8),
                (2, 9),
                (3, 4),
                (3, 5),
                (3, 6),
                (3, 7),
                (3, 8),
                (3, 9),
                (4, 5),
                (4, 6),
                (4, 7),
                (4, 8),
                (4, 9),
                (5, 6),
                (5, 7),
                (5, 8),
                (5, 9),
                (6, 7),
                (6, 8),
                (6, 9),
                (7, 8),
                (7, 9),
                (8, 9)
            ],
            list(unique_pairs_of_n_digit_numbers(1))
        )