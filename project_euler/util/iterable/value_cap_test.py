from unittest import TestCase

from project_euler.util.iterable.value_cap import value_cap

class TestValueCap(TestCase):
    def test_value_cap(self):
        self.assertEqual(list(range(1, 11)), list(value_cap(10, range(1, 11))))
        self.assertEqual(list(range(1, 6)), list(value_cap(5, range(1, 11))))
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], list(value_cap(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
        self.assertEqual([1, 2, 3, 4, 5], list(value_cap(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
