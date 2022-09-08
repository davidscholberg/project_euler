from ..util.primes import is_prime, SieveOfEritosthenesIterator

def get_answer() -> int:
    coefficient_a = 0
    coefficient_b = 0
    max_consecutive_primes = 0
    for prime in SieveOfEritosthenesIterator(1000):
        for coefficient in range(-999, 1000):
            consecutive_primes = 1
            n = 1
            while is_prime((n ** 2) + (coefficient * n) + prime):
                consecutive_primes += 1
                n += 1
            if consecutive_primes > max_consecutive_primes:
                max_consecutive_primes = consecutive_primes
                coefficient_a = coefficient
                coefficient_b = prime
    return coefficient_a * coefficient_b