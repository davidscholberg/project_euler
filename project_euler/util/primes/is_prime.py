import math

# https://en.wikipedia.org/wiki/Primality_test#Simple_methods
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.floor(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True