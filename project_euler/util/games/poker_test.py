from unittest import TestCase

from project_euler.util.games.poker import Card, Hand

class TestPoker(TestCase):
    def test_card(self):
        self.assertRaises(ValueError, lambda: Card("123"))
        self.assertRaises(ValueError, lambda: Card("0H"))
        self.assertRaises(ValueError, lambda: Card("1H"))
        self.assertRaises(ValueError, lambda: Card("FH"))
        self.assertRaises(ValueError, lambda: Card("2B"))
        self.assertEqual(Card("2H").value, 2)
        self.assertEqual(Card("TH").value, 10)
        self.assertEqual(Card("2H").suit, "H")
        self.assertEqual(Card("2H"), Card("2H"))
        self.assertLess(Card("QC"), Card("AS"))

    def test_hand(self):
        self.assertLess(
            Hand((Card("5H"), Card("5C"), Card("6S"), Card("7S"), Card("KD"))),
            Hand((Card("2C"), Card("3S"), Card("8S"), Card("8D"), Card("TD")))
        )
        self.assertGreater(
            Hand((Card("5D"), Card("8C"), Card("9S"), Card("JS"), Card("AC"))),
            Hand((Card("2C"), Card("5C"), Card("7D"), Card("8S"), Card("QH")))
        )
        self.assertLess(
            Hand((Card("2D"), Card("9C"), Card("AS"), Card("AH"), Card("AC"))),
            Hand((Card("3D"), Card("6D"), Card("7D"), Card("TD"), Card("QD")))
        )
        self.assertGreater(
            Hand((Card("4D"), Card("6S"), Card("9H"), Card("QH"), Card("QC"))),
            Hand((Card("3D"), Card("6D"), Card("7H"), Card("QD"), Card("QS")))
        )
        self.assertGreater(
            Hand((Card("2H"), Card("2D"), Card("4C"), Card("4D"), Card("4S"))),
            Hand((Card("3C"), Card("3D"), Card("3S"), Card("9S"), Card("9D")))
        )