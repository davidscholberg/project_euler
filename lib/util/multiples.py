import math

def factorial(n: int) -> int:
    return math.prod(range(1, n + 1))

def get_factors(n: int) -> tuple:
    factors = get_proper_divisors(n)
    if n > 1:
        factors = list(factors)
        factors.append(n)
        factors = tuple(factors)
    return factors

def get_list_of_multiples_capped(multiple_of, multiple_cap):
    current_multiple = multiple_of
    list_of_multiples = []
    while current_multiple < multiple_cap:
        list_of_multiples.append(current_multiple)
        current_multiple += multiple_of
    return list_of_multiples

def get_proper_divisors(n: int) -> tuple:
    proper_divisors = [1]
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            proper_divisors.append(i)
            proper_divisors.append(n // i)
    return tuple(proper_divisors)