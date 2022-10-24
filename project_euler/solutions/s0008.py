import math

from project_euler.paths import get_data_file_path
from project_euler.util.digits.digits import digits
from project_euler.util.iterable.sliding_window import sliding_window

def get_answer() -> int:
    with open(get_data_file_path('1000_digit_number.txt')) as file:
        number = int(file.read())
        return max(sliding_window(digits(number), 13, math.prod))