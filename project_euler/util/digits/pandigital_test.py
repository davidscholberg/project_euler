from unittest import TestCase

from project_euler.util.digits.pandigital import is_pandigital, max_pandigital, min_pandigital

class TestPandigital(TestCase):
    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(1))
        self.assertTrue(is_pandigital(21))
        self.assertTrue(is_pandigital(132))
        self.assertTrue(is_pandigital(3412))
        self.assertFalse(is_pandigital(10))
        self.assertFalse(is_pandigital(24))
        self.assertFalse(is_pandigital(34321))
        self.assertTrue(is_pandigital((1,)))
        self.assertTrue(is_pandigital((2, 1)))
        self.assertTrue(is_pandigital((1, 3, 2)))
        self.assertTrue(is_pandigital((3, 4, 1, 2)))
        self.assertFalse(is_pandigital((1, 0)))
        self.assertFalse(is_pandigital((3, 4, 3, 2, 1)))

    def test_min_max_pandigital(self):
        self.assertEqual(1, min_pandigital(1))
        self.assertEqual(12, min_pandigital(2))
        self.assertEqual(123, min_pandigital(3))
        self.assertEqual(1, max_pandigital(1))
        self.assertEqual(21, max_pandigital(2))
        self.assertEqual(321, max_pandigital(3))