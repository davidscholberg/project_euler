from unittest import TestCase

from project_euler.util.digits.digit_permutation import is_digit_permutation

class TestDigitPermutation(TestCase):
    def test_is_digit_permutation(self):
        self.assertTrue(is_digit_permutation(1234, 2143))
        self.assertTrue(is_digit_permutation(5224, 2452))
        self.assertFalse(is_digit_permutation(1234, 2243))
        self.assertFalse(is_digit_permutation(1234, 3251))
        self.assertFalse(is_digit_permutation(1234, 3255))
        self.assertFalse(is_digit_permutation(1234, 5678))
        self.assertFalse(is_digit_permutation(17173512, 25153757))