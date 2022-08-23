from lib.util.digits import is_palindromic_number

def get_largest_palindromic_number_from_product_of_two_three_digit_numbers() -> int:
    largest_palindromic_number = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            n = i * j
            if is_palindromic_number(n) and n > largest_palindromic_number:
                largest_palindromic_number = n
    return largest_palindromic_number

def get_answer() -> int:
    return get_largest_palindromic_number_from_product_of_two_three_digit_numbers()