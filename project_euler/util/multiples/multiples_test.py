from unittest import TestCase

from project_euler.util.multiples.multiples import multiples

class TestMultiples(TestCase):
    def test_multiples(self):
        for i in range(1, 11):
            multiples_iterator = multiples(i)
            previous_multiple = 0
            for _ in range(1, 11):
                multiple = next(multiples_iterator)
                self.assertEqual(multiple - previous_multiple, i)
                self.assertEqual(multiple % i, 0)
                previous_multiple = multiple
