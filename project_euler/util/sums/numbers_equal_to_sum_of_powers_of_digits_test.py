from unittest import TestCase

from project_euler.util.sums.numbers_equal_to_sum_of_powers_of_digits import numbers_equal_to_sum_of_powers_of_digits

class TestNumbersEqualToSumOfPowersOfDigits(TestCase):
    def test_numbers_equal_to_sum_of_powers_of_digits(self):
        self.assertEqual((153, 370, 371, 407), tuple(numbers_equal_to_sum_of_powers_of_digits(3)))