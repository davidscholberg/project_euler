import math

def factorial(n: int) -> int:
    return math.prod(range(1, n + 1))

def get_factors(n: int) -> tuple:
    factors = [1]
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    if n > 1:
        factors.append(n)
    return tuple(factors)

def get_list_of_multiples_capped(multiple_of, multiple_cap):
    current_multiple = multiple_of
    list_of_multiples = []
    while current_multiple < multiple_cap:
        list_of_multiples.append(current_multiple)
        current_multiple += multiple_of
    return list_of_multiples

def get_proper_divisors(n: int) -> tuple:
    factors = set(get_factors(n))
    if n > 1:
        factors = filter(lambda x: x != n, factors)
    return tuple(factors)