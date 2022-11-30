from unittest import TestCase

from project_euler.util.sums.digit_factorial_sum import digit_factorial_sum

class TestDigitFactorialSum(TestCase):
    def test_digit_factorial_sum(self):
        self.assertEqual(409114, digit_factorial_sum(1234567890))