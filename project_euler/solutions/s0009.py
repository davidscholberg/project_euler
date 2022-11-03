import math

from project_euler.util.iterable.nth import nth
from project_euler.util.sums.pythagorean_triplet import is_pythagorean_triplet
from project_euler.util.sums.split_number import split_number

def get_answer() -> int:
    triplet = nth(
        1,
        filter(
            is_pythagorean_triplet,
            split_number(1000, ways=3, distinct=True)
        )
    )
    return math.prod(triplet)