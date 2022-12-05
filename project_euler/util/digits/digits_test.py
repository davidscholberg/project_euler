from unittest import TestCase

from project_euler.util.digits.digits import append_digit, digit_count, digits, digits_c_wrapper, number_from_digits

class TestDigits(TestCase):
    def test_append_digit(self):
        self.assertEqual(10, append_digit(1, 0))
        self.assertEqual(12345, append_digit(1234, 5))

    def test_digit_count(self):
        self.assertEqual(1, digit_count(0))
        self.assertEqual(1, digit_count(1))
        self.assertEqual(1, digit_count(2))
        self.assertEqual(1, digit_count(8))
        self.assertEqual(1, digit_count(9))
        self.assertEqual(2, digit_count(10))
        self.assertEqual(2, digit_count(11))
        self.assertEqual(2, digit_count(12))
        self.assertEqual(2, digit_count(98))
        self.assertEqual(2, digit_count(99))
        self.assertEqual(3, digit_count(100))
        self.assertEqual(3, digit_count(101))
        self.assertEqual(3, digit_count(102))
        self.assertEqual(3, digit_count(998))
        self.assertEqual(3, digit_count(999))
        self.assertEqual(4, digit_count(1000))
        self.assertEqual(4, digit_count(1001))
        self.assertEqual(4, digit_count(1002))

    def test_digits(self):
        self.assertEqual((0,), digits(0))
        self.assertEqual((1,), digits(1))
        self.assertEqual((9,), digits(9))
        self.assertEqual((1, 0), digits(10))
        self.assertEqual((2, 0), digits(20))
        self.assertEqual((3, 8), digits(38))
        self.assertEqual((9, 4, 3, 0, 5, 9, 3, 9, 8), digits(943059398))

    def test_digits_c(self):
        self.assertEqual((0,), digits_c_wrapper(0))
        self.assertEqual((1,), digits_c_wrapper(1))
        self.assertEqual((9,), digits_c_wrapper(9))
        self.assertEqual((1, 0), digits_c_wrapper(10))
        self.assertEqual((2, 0), digits_c_wrapper(20))
        self.assertEqual((3, 8), digits_c_wrapper(38))
        self.assertEqual((9, 4, 3, 0, 5, 9, 3, 9, 8), digits_c_wrapper(943059398))

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