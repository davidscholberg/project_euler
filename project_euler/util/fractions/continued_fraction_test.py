from itertools import chain, repeat
from unittest import TestCase

from project_euler.util.fractions.continued_fraction import ContinuedFraction

class TestContinuedFraction(TestCase):
    def test_continued_fraction(self):
        get_a_terms = lambda: repeat(1)
        get_b_terms = lambda: chain((1,), repeat(2))
        continued_fraction = ContinuedFraction(get_a_terms, get_b_terms, starting_cache_depth=1)
        self.assertEqual(continued_fraction.calculate(0), (3, 2))
        self.assertEqual(continued_fraction.calculate(1), (7, 5))
        self.assertEqual(continued_fraction.calculate(2), (17, 12))
        self.assertEqual(continued_fraction.calculate(3), (41, 29))