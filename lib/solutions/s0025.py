from ..util.digits import get_number_of_digits
from ..util.sequences import FibonacciIterator

def get_answer() -> int:
    for i, term in enumerate(FibonacciIterator()):
        if get_number_of_digits(term) == 1000:
            return i + 1