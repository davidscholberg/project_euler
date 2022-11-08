from project_euler.util.multiples.abundant_numbers import non_abundant_sum_numbers

def get_answer() -> int:
    return sum(non_abundant_sum_numbers(28123))