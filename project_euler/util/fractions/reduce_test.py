from unittest import TestCase

from project_euler.util.fractions.reduce import reduce_fraction

class TestReduce(TestCase):
    def test_reduce_fraction(self):
        self.assertEqual((1, 2), reduce_fraction((7, 14)))
        self.assertEqual((5, 9), reduce_fraction((1560, 2808)))
        self.assertEqual((13, 6), reduce_fraction((156, 72)))