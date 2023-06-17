from unittest import TestCase

from project_euler.util.cryptography.cipher import xor_cipher

class TestCipher(TestCase):
    def test_xor_cipher(self):
        plaintext = b"Project Euler"
        password = b"xor"
        ciphertext = xor_cipher(plaintext, password)
        self.assertEqual(ciphertext, b"\x28\x1D\x1D\x12\x0A\x11\x0C\x4F\x37\x0D\x03\x17\x0A")
        self.assertEqual(xor_cipher(ciphertext, password), plaintext)