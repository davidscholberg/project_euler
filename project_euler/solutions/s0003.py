from project_euler.util.primes.prime_factors import prime_factors

def get_answer() -> int:
    return max(prime_factors(600851475143))
