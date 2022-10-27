from project_euler.util.multiples.factors import factors
from project_euler.util.sequences.triangle_numbers import triangle_numbers

def get_answer() -> int:
    for triangle_number in triangle_numbers():
        if len(list(factors(triangle_number))) > 500:
            return triangle_number