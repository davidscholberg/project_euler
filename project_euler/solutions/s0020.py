from project_euler.util.digits.digits import digits
from project_euler.util.multiples.factorial import factorial

def get_answer() -> int:
    return sum(digits(factorial(100)))