import math

from project_euler.util.sums.pythagorean_triplet import pythagorean_triplets

def get_answer() -> int:
    triplet = pythagorean_triplets(1000)[0]
    return math.prod(triplet)