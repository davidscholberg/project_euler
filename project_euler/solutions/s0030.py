from project_euler.util.sums.numbers_equal_to_sum_of_powers_of_digits import numbers_equal_to_sum_of_powers_of_digits

def get_answer() -> int:
    return sum(numbers_equal_to_sum_of_powers_of_digits(5))