from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.primes.circular_primes import circular_primes

def get_answer() -> int:
    return iter_len(circular_primes(999999))