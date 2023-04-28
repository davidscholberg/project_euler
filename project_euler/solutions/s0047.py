from itertools import count

from project_euler.util.primes.prime_factors import prime_factors_int

def get_answer() -> int:
    consecutive = 0
    for n in count(4):
        if len(set(prime_factors_int(n))) == 4:
            consecutive += 1
        else:
            consecutive = 0
        if consecutive == 4:
            return n - 3
    return 0