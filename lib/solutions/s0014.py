from ..util.sequences import get_number_of_collatz_terms

# This could be made more efficient by caching collatz terms whose sequences have already been calculated.
def get_number_with_max_number_of_collatz_terms_in_range(start: int, end: int) -> int:
    max_collatz_terms = 0
    max_collatz_terms_number = 0
    for i in range(start, end + 1):
        collatz_terms = get_number_of_collatz_terms(i)
        if collatz_terms > max_collatz_terms:
            max_collatz_terms = collatz_terms
            max_collatz_terms_number = i
    return max_collatz_terms_number

def get_answer() -> int:
    return get_number_with_max_number_of_collatz_terms_in_range(1, 999999)