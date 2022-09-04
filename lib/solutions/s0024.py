from ..util.digits import get_number_from_digits
from ..util.sequences import get_nth_permutation

def get_answer() -> int:
    nth_permutation = get_nth_permutation((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 1000000)
    return get_number_from_digits(nth_permutation)