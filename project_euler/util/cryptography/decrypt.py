from typing import Callable

def letter_frequency(letter: str) -> float:
    """
    Returns the frequency which the given letter occurs in English texts.

    If the character is not alphabetical, zero is returned. If the string length
    is not 1, ValueError is raised.

    Frequency values copied from https://en.wikipedia.org/wiki/Letter_frequency.
    """
    if len(letter) != 1:
        raise ValueError(f"invalid letter {letter}")
    if not letter.isalpha():
        return 0
    match letter.upper():
        case "A":
            return 0.082
        case "B":
            return 0.015
        case "C":
            return 0.028
        case "D":
            return 0.043
        case "E":
            return 0.127
        case "F":
            return 0.022
        case "G":
            return 0.02
        case "H":
            return 0.061
        case "I":
            return 0.07
        case "J":
            return 0.0015
        case "K":
            return 0.0077
        case "L":
            return 0.04
        case "M":
            return 0.024
        case "N":
            return 0.067
        case "O":
            return 0.075
        case "P":
            return 0.019
        case "Q":
            return 0.00095
        case "R":
            return 0.06
        case "S":
            return 0.063
        case "T":
            return 0.091
        case "U":
            return 0.028
        case "V":
            return 0.0098
        case "W":
            return 0.024
        case "X":
            return 0.0015
        case "Y":
            return 0.02
        case "Z":
            return 0.00074
        case _:
            return 0

def guess_password(
    ciphertext: bytes,
    decipher: Callable[[bytes, bytes], bytes],
    password_length: int,
    allowed_password_bytes: bytes
) -> bytes:
    """
    Attempt to guess the password used to generate the ciphertext, using the
    given decipher function, the password length, and the range of allowed
    password byte values.
    """
    password_bytes = []
    for i in range(password_length):
        sliced_ciphertext = bytes(ciphertext[i::password_length])
        high_ascii_score = -1
        best_candidate_byte = None
        for password_byte in allowed_password_bytes:
            sliced_plaintext = decipher(sliced_ciphertext, bytes((password_byte,)))
            ascii_score = sum(map(lambda b: letter_frequency(chr(b)), sliced_plaintext))
            if ascii_score > high_ascii_score:
                high_ascii_score = ascii_score
                best_candidate_byte = password_byte
        password_bytes.append(best_candidate_byte)
    return bytes(password_bytes)