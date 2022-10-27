from unittest import TestCase

from project_euler.util.multiples.factors import factors

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