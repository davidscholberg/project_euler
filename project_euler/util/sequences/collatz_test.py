from unittest import TestCase

from project_euler.util.sequences.collatz import Collatz, collatz, collatz_sequence

class TestCollatz(TestCase):
    def test_collatz(self):
        self.assertEqual(1, collatz(2))
        self.assertEqual(10, collatz(3))
        self.assertEqual(2, collatz(4))
        self.assertEqual(16, collatz(5))
        self.assertEqual([13, 40, 20, 10, 5, 16, 8, 4, 2, 1], list(collatz_sequence(13)))
        collatz_instance = Collatz()
        self.assertEqual(1, collatz_instance.sequence_length(1))
        self.assertEqual(2, collatz_instance.sequence_length(2))
        self.assertEqual(8, collatz_instance.sequence_length(3))
        self.assertEqual(3, collatz_instance.sequence_length(4))
        self.assertEqual(6, collatz_instance.sequence_length(5))