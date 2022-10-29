from unittest import TestCase

from project_euler.util.words.number_words import number_words

class TestNumberWords(TestCase):
    def test_number_words(self):
        self.assertEqual('zero', number_words(0))
        self.assertEqual('one', number_words(1))
        self.assertEqual('ten', number_words(10))
        self.assertEqual('eleven', number_words(11))
        self.assertEqual('twenty', number_words(20))
        self.assertEqual('twenty one', number_words(21))
        self.assertEqual('one hundred', number_words(100))
        self.assertEqual('one hundred and one', number_words(101))
        self.assertEqual('one hundred and ten', number_words(110))
        self.assertEqual('one hundred and twenty', number_words(120))
        self.assertEqual('one hundred and twenty one', number_words(121))
        self.assertEqual('one thousand', number_words(1000))
        self.assertEqual('one thousand and one', number_words(1001))
        self.assertEqual('one thousand and ten', number_words(1010))
        self.assertEqual('one thousand and eleven', number_words(1011))
        self.assertEqual('one thousand and twenty', number_words(1020))
        self.assertEqual('one thousand and twenty one', number_words(1021))
        self.assertEqual('one thousand one hundred', number_words(1100))
        self.assertEqual('one thousand one hundred and one', number_words(1101))
        self.assertEqual('one thousand one hundred and ten', number_words(1110))
        self.assertEqual('one thousand one hundred and twenty', number_words(1120))
        self.assertEqual('one thousand one hundred and twenty one', number_words(1121))