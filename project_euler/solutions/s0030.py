from project_euler.util.sums.digit_power_sum_numbers import digit_power_sum_numbers

def get_answer() -> int:
    return sum(digit_power_sum_numbers(5))