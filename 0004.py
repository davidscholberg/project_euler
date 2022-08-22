from lib.get_digits import GetDigitsIterator

def is_palindromic_number(n: int) -> bool:
    if n < 10:
        return True
    reverse_n = 0
    for digit in GetDigitsIterator(n, reverse = True):
        reverse_n = (reverse_n * 10) + digit
    return reverse_n == n

def get_largest_palindromic_number_from_product_of_two_three_digit_numbers() -> int:
    largest_palindromic_number = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            n = i * j
            if is_palindromic_number(n) and n > largest_palindromic_number:
                largest_palindromic_number = n
    return largest_palindromic_number

answer = get_largest_palindromic_number_from_product_of_two_three_digit_numbers()
print(answer)