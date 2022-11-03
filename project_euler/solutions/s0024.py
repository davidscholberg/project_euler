from project_euler.util.digits.digits import number_from_digits
from project_euler.util.iterable.nth import nth
from project_euler.util.sequences.permutations import permutations

def get_answer() -> int:
    return number_from_digits(nth(1000000, permutations(range(0, 10))))