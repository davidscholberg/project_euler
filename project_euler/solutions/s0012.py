from project_euler.util.iterable.nth import nth
from project_euler.util.multiples.factors import factors
from project_euler.util.sequences.triangle_numbers import triangle_numbers

def get_answer() -> int:
    return nth(
        1,
        filter(
            lambda triangle_number: len(factors(triangle_number)) > 500,
            triangle_numbers()
        )
    )