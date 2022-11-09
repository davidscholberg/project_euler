from unittest import TestCase

from project_euler.util.sequences.rotations import rotations

class TestRotations(TestCase):
    def test_rotations(self):
        self.assertEqual(
            (
                (1, 2, 3, 4),
                (4, 1, 2, 3),
                (3, 4, 1, 2),
                (2, 3, 4, 1)
            ),
            tuple(rotations(range(1, 5)))
        )