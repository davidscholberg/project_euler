from unittest import TestCase

from project_euler.util.digits.base_convert import base_convert

class TestBaseConvert(TestCase):
    def test_base_convert(self):
        self.assertEqual(100, base_convert(1001, 2, 3))
        self.assertEqual(256540, base_convert(23231032, 4, 7))
        self.assertEqual(298, base_convert(100101010, 2, 10))
        self.assertEqual(10010100011111, base_convert(9503, 10, 2))
        self.assertEqual(2430014, base_convert(45634, 10, 5))