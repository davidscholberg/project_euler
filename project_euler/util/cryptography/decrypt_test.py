from unittest import TestCase

from project_euler.util.cryptography.cipher import xor_cipher
from project_euler.util.cryptography.decrypt import guess_password, letter_frequency

class TestDecrypt(TestCase):
    def test_guess_password(self):
        plaintext = b"Project Euler exists to encourage, challenge, and develop the skills and enjoyment of anyone with an interest in the fascinating world of mathematics."
        password = b"xor"
        ciphertext = xor_cipher(plaintext, password)
        guessed_password = guess_password(ciphertext, xor_cipher, 3, bytes(range(97, 123)))
        self.assertEqual(guessed_password, password)

    def test_letter_frequency(self):
        self.assertRaises(ValueError, lambda: letter_frequency("asdf"))
        self.assertEqual(letter_frequency("*"), 0)
        self.assertEqual(letter_frequency("e"), 0.127)