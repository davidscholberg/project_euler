from unittest import TestCase

from project_euler.util.multiples.multiples import multiples, smallest_number_divisible_by

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
        self.assertEqual(2, next(multiples(2, minimum=1)))
        self.assertEqual(2, next(multiples(2, minimum=2)))
        self.assertEqual(4, next(multiples(2, minimum=3)))

    def test_smallest_number_divisible_by(self):
        self.assertEqual(2520, smallest_number_divisible_by(range(2, 11)))