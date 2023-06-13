from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.digits.palindrome import is_palindromic_number

def is_lychrel_number(n: int, non_lychrel_cache: set | None = None) -> bool:
    """
    Tells whether or not n is a lychrel number.

    Optionally, you can pass in a set to have this function cache all of the
    non-lychrel numbers it encounters.

    A lychrel number is one in which the following process never* produces a
    palindromic number: take n, reverse the digits and add the resulting number
    to n, repeat on the result until the result is palindromic.

    * It hasn't yet been proved that there are lychrel numbers, so for now we
    assume that any n that takes 50 or more iterations to arrive at a palindrome
    is a lychrel number.
    """
    current_result = n
    addends = []
    if non_lychrel_cache is not None:
        pass
    for _ in range(49):
        reverse_n = number_from_digits(reversed(digits(current_result)))
        if non_lychrel_cache is not None:
            addends.extend((current_result, reverse_n))
        current_result += reverse_n
        if is_palindromic_number(current_result):
            if non_lychrel_cache is not None:
                non_lychrel_cache.update(addends)
            return False
    return True