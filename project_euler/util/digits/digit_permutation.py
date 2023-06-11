from project_euler.util.digits.digits import digits

def is_digit_permutation(n: int, m: int) -> bool:
    """
    Tells whether m is a digit permutation of n.

    It is assumed that n and m have the same number of digits.
    """
    n_digit_dict = dict.fromkeys(digits(n))
    m_digit_dict = dict.fromkeys(digits(m))
    if len(n_digit_dict) != len(m_digit_dict):
        return False
    for n_digit in n_digit_dict:
        if n_digit not in m_digit_dict:
            return False
    return True