from project_euler.util.digits.n_digit_number import unique_pairs_of_n_digit_numbers
from project_euler.util.digits.palindrome import is_palindromic_number

def get_answer() -> int:
    return max(filter(is_palindromic_number, map(lambda t: t[0] * t[1], unique_pairs_of_n_digit_numbers(3))))