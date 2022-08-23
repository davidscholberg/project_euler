from ..util.multiples import get_factors
from ..util.sequences import TriangleNumberIterator

def get_first_triangle_number_with_over_n_divisors(n: int) -> int:
    for triangle_number in TriangleNumberIterator():
        if len(get_factors(triangle_number)) > n:
            return triangle_number

def get_answer() -> int:
    return get_first_triangle_number_with_over_n_divisors(500)