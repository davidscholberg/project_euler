from unittest import TestCase

from project_euler.util.digits.concatenate import concatenate_integers

class TestConcatenate(TestCase):
    def test_concatenate_integers(self):
        self.assertEqual(concatenate_integers(2, 30), 230)
        self.assertEqual(concatenate_integers(30, 2), 302)
        self.assertEqual(concatenate_integers(30, 30), 3030)