from project_euler.paths import data_file_path
from project_euler.util.cryptography.cipher import xor_cipher
from project_euler.util.cryptography.decrypt import guess_password

def get_answer() -> int:
    with open(data_file_path('ciphertext_int_array.txt')) as f:
        ciphertext = bytes(map(int, f.read().split(",")))
        password = guess_password(ciphertext, xor_cipher, 3, bytes(range(97, 123)))
        plaintext = xor_cipher(ciphertext, password)
        return sum(plaintext)