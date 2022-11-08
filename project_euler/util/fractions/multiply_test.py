from unittest import TestCase

from project_euler.util.fractions.multiply import multiply_fractions

class TestMultiply(TestCase):
    def test_multiply_fractions(self):
        self.assertEqual((91, 56), multiply_fractions((7, 14), (13, 4)))