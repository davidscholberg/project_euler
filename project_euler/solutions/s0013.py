from project_euler.paths import data_file_path
from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.iterable.count_cap import count_cap

def get_answer() -> int:
    with open(data_file_path('50_digit_numbers.txt')) as file:
        sum_of_numbers = sum(map(int, file))
        return number_from_digits(count_cap(10, digits(sum_of_numbers)))