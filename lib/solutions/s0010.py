from ..util.primes import SieveOfEritosthenesIterator

def get_answer() -> int:
    return sum(SieveOfEritosthenesIterator(1999999))