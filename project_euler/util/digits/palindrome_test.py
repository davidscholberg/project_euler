from unittest import TestCase

from project_euler.util.digits.palindrome import is_palindromic_number

class TestPalindrome(TestCase):
    def test_is_palindromic_number(self):
        self.assertTrue(is_palindromic_number(1))
        self.assertTrue(is_palindromic_number(202))
        self.assertTrue(is_palindromic_number(940234432049))
        self.assertFalse(is_palindromic_number(10))
        self.assertFalse(is_palindromic_number(324))
        self.assertFalse(is_palindromic_number(7345937845))