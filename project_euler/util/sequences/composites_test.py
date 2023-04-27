from unittest import TestCase

from project_euler.util.iterable.count_cap import count_cap
from project_euler.util.sequences.composites import odd_composites

class TestComposites(TestCase):
    def test_odd_composites(self):
        self.assertEqual([9, 15, 21, 25, 27, 33], list(count_cap(6, odd_composites())))