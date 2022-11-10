def is_palindromic_number(n: int) -> bool:
    if n < 10:
        return True
    n_str = str(n)
    digits_count_of_n = len(n_str)
    half_digit_count = digits_count_of_n // 2
    even_offset = 1 if digits_count_of_n % 2 == 0 else 0
    for i, mirror in zip(range(0, half_digit_count), range(digits_count_of_n - 1, half_digit_count - even_offset, -1)):
        if n_str[i] != n_str[mirror]:
            return False
    return True