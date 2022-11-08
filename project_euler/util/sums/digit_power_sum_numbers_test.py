from unittest import TestCase

from project_euler.util.sums.digit_power_sum_numbers import digit_power_sum_numbers

class TestDigitPowerSumNumbers(TestCase):
    def test_digit_power_sum_numbers(self):
        self.assertEqual((153, 370, 371, 407), tuple(digit_power_sum_numbers(3)))