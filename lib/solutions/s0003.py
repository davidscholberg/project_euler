from ..util.primes import get_prime_factors

def get_largest_prime_factor(n: int) -> int:
    return get_prime_factors(n)[-1]

def get_answer() -> int:
    return get_largest_prime_factor(600851475143)