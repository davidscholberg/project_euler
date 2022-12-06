from project_euler.util.multiples.factors import factors

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return len(factors(n, proper=True)) == 1