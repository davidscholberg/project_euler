from unittest import TestCase

from project_euler.util.words.word_scores import word_score, word_scores

class TestWordScores(TestCase):
    def test_word_score(self):
        self.assertEqual(20, word_score(5, 'aaaa'))
        self.assertEqual(20, word_score(5, 'AAAA'))
        self.assertEqual(67000, word_score(1000, 'TheDude'))

    def test_word_scores(self):
        self.assertEqual(
            (4, 134, 12),
            tuple(word_scores(('aaaa', 'AAAA', 'TheDude')))
        )