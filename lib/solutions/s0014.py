from ..util.sequences import Collatz

def get_number_with_max_number_of_collatz_terms_in_range(start: int, end: int) -> int:
    collatz = Collatz()
    max_collatz_terms = 0
    max_collatz_terms_number = 0
    for i in range(end, start - 1, -1):
        collatz_terms = collatz.get_number_of_collatz_terms(i)
        if collatz_terms > max_collatz_terms:
            max_collatz_terms = collatz_terms
            max_collatz_terms_number = i
    return max_collatz_terms_number

def get_answer() -> int:
    return get_number_with_max_number_of_collatz_terms_in_range(1, 999999)