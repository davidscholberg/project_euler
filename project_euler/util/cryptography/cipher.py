from itertools import cycle, starmap
from operator import xor

def xor_cipher(text: bytes, password: bytes) -> bytes:
    """
    Reciprocal cipher using xor on each byte. The password is repeated to fit
    the text.
    """
    return bytes(starmap(xor, zip(text, cycle(password))))