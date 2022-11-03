from project_euler.util.multiples.abundant_numbers import numbers_not_sum_of_two_abundant_numbers

def get_answer() -> int:
    return sum(numbers_not_sum_of_two_abundant_numbers(28123))