from unittest import TestCase

from project_euler.util.digits.concatenated_product import concatenated_product

class TestConcatenatedProduct(TestCase):
    def test_concatenated_product(self):
        self.assertEqual(12345, concatenated_product(1, (1, 2, 3, 4, 5)))
        self.assertEqual(55847, concatenated_product(11, (5, 77)))