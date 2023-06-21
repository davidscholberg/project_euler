from project_euler.util.digits.digits import digit_count_map

def is_digit_permutation(n: int, m: int) -> bool:
    """Tells whether m is a digit permutation of n."""
    return digit_count_map(n) == digit_count_map(m)