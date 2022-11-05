from itertools import starmap

from project_euler.util.digits.digits import digit_count
from project_euler.util.iterable.nth import nth
from project_euler.util.sequences.fibonacci import fibonacci

def get_answer() -> int:
    return nth(
        1,
        starmap(
            lambda term_number, _: term_number,
            filter(
                lambda t: digit_count(t[1]) == 1000,
                enumerate(fibonacci(), start=1)
            )
        )
    )