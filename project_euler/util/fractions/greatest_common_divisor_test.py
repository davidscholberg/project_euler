from unittest import TestCase

from project_euler.util.fractions.greatest_common_divisor import greatest_common_divisor

class TestGreatestCommonDivisor(TestCase):
    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor((8, 12)), 4)
        self.assertEqual(greatest_common_divisor((54, 24)), 6)
        self.assertEqual(greatest_common_divisor((42, 56)), 14)
        self.assertEqual(greatest_common_divisor((48, 18)), 6)