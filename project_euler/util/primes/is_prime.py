from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.multiples.factors import factors

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return iter_len(factors(n, proper=True)) == 1