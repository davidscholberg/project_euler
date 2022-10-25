from unittest import TestCase

from project_euler.util.sums.pythagorean_triplet import is_pythagorean_triplet

class TestPythagoreanTriplet(TestCase):
    def test_is_pythagorean_triplet(self):
        self.assertTrue(is_pythagorean_triplet((3, 4, 5)))
        self.assertTrue(is_pythagorean_triplet((9, 40, 41)))
        self.assertFalse(is_pythagorean_triplet((12, 13, 748659)))