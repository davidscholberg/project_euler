from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.multiples.factors import factors

def is_prime(n: int) -> bool:
    return n > 1 and iter_len(factors(n, proper=True)) == 1