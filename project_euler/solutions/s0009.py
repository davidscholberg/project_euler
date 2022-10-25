import math

from project_euler.util.sums.pythagorean_triplet import is_pythagorean_triplet
from project_euler.util.sums.split_number import split_number

def get_answer() -> int:
    for triplet in split_number(1000, ways=3, ascending=True):
        if is_pythagorean_triplet(triplet):
            return math.prod(triplet)