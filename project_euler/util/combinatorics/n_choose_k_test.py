from unittest import TestCase

from project_euler.util.combinatorics.n_choose_k import n_choose_k

class TestNChooseK(TestCase):
    def test_n_choose_k(self):
        self.assertEqual(n_choose_k(5, 3), 10)
        self.assertEqual(n_choose_k(23, 10), 1144066)
        self.assertEqual(n_choose_k(100, 3), 161700)
        self.assertEqual(n_choose_k(100, 98), 4950)