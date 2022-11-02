from unittest import TestCase

from project_euler.util.multiples.factors import factors, amicable_numbers, amicable_pairs, is_amicable_pair

class TestFactors(TestCase):
    def test_factors(self):
        self.assertEqual([1], sorted(factors(1)))
        self.assertEqual([1, 2], sorted(factors(2)))
        self.assertEqual([1, 3], sorted(factors(3)))
        self.assertEqual([1, 2, 4], sorted(factors(4)))
        self.assertEqual([1, 5], sorted(factors(5)))
        self.assertEqual([1, 2, 3, 6], sorted(factors(6)))
        self.assertEqual([1, 7], sorted(factors(7)))
        self.assertEqual([1, 2, 4, 8], sorted(factors(8)))
        self.assertEqual([1, 3, 9], sorted(factors(9)))
        self.assertEqual([1, 2, 5, 10], sorted(factors(10)))
        self.assertEqual([1, 2, 3, 4, 6], sorted(factors(12, proper=True)))

    def test_amicable_numbers(self):
        self.assertEqual((220, 284, 1184, 1210, 2620, 2924), tuple(amicable_numbers(1, 3000)))

    def test_amicable_pairs(self):
        self.assertEqual(
            (
                (220, 284),
                (1184, 1210),
                (2620, 2924)
            ),
            tuple(amicable_pairs(1, 3000))
        )

    def test_is_amicable_pair(self):
        self.assertTrue(is_amicable_pair(220, 284))
        self.assertTrue(is_amicable_pair(1184, 1210))
        self.assertTrue(is_amicable_pair(2620, 2924))
        self.assertFalse(is_amicable_pair(2, 2))
        self.assertFalse(is_amicable_pair(87, 48))