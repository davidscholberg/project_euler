from itertools import repeat
from typing import Callable

from project_euler.util.digits.concatenate import concatenate_integers

def cyclical_figurates(
    figurate_tests: tuple[Callable[[int], bool], ...],
    previous_term: int | None = None,
    first_term: int | None = None
) -> tuple[int, ...]:
    """
    Find the first ordered set of 4-digit numbers whose members are each a
    different figurate and whose last two digits match the first two digits of
    the next member (with the last member wrapping around to the first).

    The previous term and first term arguments are meant to be set internally,
    as this is a recursive function.
    """
    if len(figurate_tests) == 1:
        if previous_term is None or first_term is None:
            raise ValueError("previous and/or first term not set")
        n = concatenate_integers(previous_term, first_term)
        if figurate_tests[0](n):
            return (n,)
        return ()
    term_a_iterator = None
    if previous_term is None:
        term_a_iterator = range(10, 100)
    else:
        term_a_iterator = iter((previous_term,))
    for term_a in term_a_iterator:
        sub_first_term = first_term if first_term is not None else term_a
        for term_b in range(10, 100):
            n = concatenate_integers(term_a, term_b)
            for figurate_test in figurate_tests:
                if figurate_test(n):
                    sub_figurate_tests = tuple(filter(lambda f: f != figurate_test, figurate_tests))
                    sub_members = cyclical_figurates(sub_figurate_tests, previous_term=term_b, first_term=sub_first_term)
                    if len(sub_members) > 0:
                        return (n,) + sub_members
    return ()