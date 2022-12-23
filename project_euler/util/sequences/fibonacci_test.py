from unittest import TestCase

from project_euler.util.sequences.fibonacci import fibonacci
from project_euler.util.iterable.value_cap import value_cap

class TestFibonacci(TestCase):
    def test_fibonacci(self):
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181], list(value_cap(4181, fibonacci())))