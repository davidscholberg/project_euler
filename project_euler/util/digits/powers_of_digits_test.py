from unittest import TestCase

from project_euler.util.digits.powers_of_digits import powers_of_digits

class TestPowersOfDigits(TestCase):
    def test_powers_of_digits(self):
        self.assertEqual((1, 2, 3, 4), tuple(powers_of_digits(1234, 1)))
        self.assertEqual((1, 4, 9, 16), tuple(powers_of_digits(1234, 2)))
        self.assertEqual((1, 8, 27, 64), tuple(powers_of_digits(1234, 3)))