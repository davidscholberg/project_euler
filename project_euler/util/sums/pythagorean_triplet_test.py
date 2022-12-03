from unittest import TestCase

from project_euler.util.sums.pythagorean_triplet import pythagorean_triplets, is_pythagorean_triplet

class TestPythagoreanTriplet(TestCase):
    def test_pythagorean_triplets(self):
        self.assertEqual(
            (
                (20, 48, 52),
                (24, 45, 51),
                (30, 40, 50),
            ),
            pythagorean_triplets(120)
        )

    def test_is_pythagorean_triplet(self):
        self.assertTrue(is_pythagorean_triplet((3, 4, 5)))
        self.assertTrue(is_pythagorean_triplet((9, 40, 41)))
        self.assertFalse(is_pythagorean_triplet((12, 13, 748659)))