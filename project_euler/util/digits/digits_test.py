from unittest import TestCase

from project_euler.util.digits.digits import digits, number_from_digits

class TestDigits(TestCase):
    def test_digits(self):
        self.assertEqual([0], list(digits(0)))
        self.assertEqual([1], list(digits(1)))
        self.assertEqual([9], list(digits(9)))
        self.assertEqual([1, 0], list(digits(10)))
        self.assertEqual([2, 0], list(digits(20)))
        self.assertEqual([3, 8], list(digits(38)))
        self.assertEqual([9, 4, 3, 0, 5, 9, 3, 9, 8], list(digits(943059398)))
        self.assertEqual([1], list(digits(1, reverse=True)))
        self.assertEqual([0, 2], list(digits(20, reverse=True)))
        self.assertEqual([8, 3], list(digits(38, reverse=True)))
        self.assertEqual([8, 9, 3, 9, 5, 0, 3, 4, 9], list(digits(943059398, reverse=True)))

    def test_number_from_digits(self):
        self.assertEqual(0, number_from_digits([0]))
        self.assertEqual(1, number_from_digits([1]))
        self.assertEqual(9, number_from_digits([9]))
        self.assertEqual(10, number_from_digits([1, 0]))
        self.assertEqual(20, number_from_digits([2, 0]))
        self.assertEqual(38, number_from_digits([3, 8]))
        self.assertEqual(943059398, number_from_digits([9, 4, 3, 0, 5, 9, 3, 9, 8]))
        self.assertEqual(1, number_from_digits(iter([1])))
        self.assertEqual(20, number_from_digits(iter([2, 0])))
        self.assertEqual(38, number_from_digits(iter([3, 8])))
        self.assertEqual(943059398, number_from_digits(iter([9, 4, 3, 0, 5, 9, 3, 9, 8])))