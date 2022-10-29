from project_euler.util.digits.digits import digits

def get_answer() -> int:
    return sum(digits(2 ** 1000))