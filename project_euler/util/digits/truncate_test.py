from unittest import TestCase

from project_euler.util.digits.truncate import left_truncate, right_truncate

class TestTruncate(TestCase):
    def test_left_truncate(self):
        self.assertEqual(0, left_truncate(310))
        self.assertEqual(1, left_truncate(311))
        self.assertEqual(10, left_truncate(310, to=2))

    def test_right_truncate(self):
        self.assertEqual(31, right_truncate(310))
        self.assertEqual(31, right_truncate(311))
        self.assertEqual(31, right_truncate(318))
        self.assertEqual(31, right_truncate(319))
        with self.assertRaises(ValueError):
            right_truncate(0)
            right_truncate(9)