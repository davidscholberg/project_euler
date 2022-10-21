from project_euler.util.digits.digits import digits, number_from_digits

def is_palindromic_number(n: int) -> bool:
    if n < 10:
        return True
    return n == number_from_digits(digits(n, reverse=True))