from ..util.digits import GetDigitsIterator

def get_answer() -> int:
    return sum(GetDigitsIterator(2 ** 1000))