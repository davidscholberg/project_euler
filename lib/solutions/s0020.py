from ..util.digits import GetDigitsIterator
from ..util.multiples import factorial

def get_answer() -> int:
    return sum(GetDigitsIterator(factorial(100)))