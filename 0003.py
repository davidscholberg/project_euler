# see sieve of eratosthenes
def get_prime_factors(n: int) -> list:
    prime_factors = []
    potential_prime_factor = 2
    while n > 1:
        if n % potential_prime_factor == 0:
            prime_factors.append(potential_prime_factor)
            n /= potential_prime_factor
        else:
            potential_prime_factor += 1
    return prime_factors

def get_largest_prime_factor(n: int) -> int:
    return get_prime_factors(n)[-1]

answer = get_largest_prime_factor(600851475143)
print(answer)