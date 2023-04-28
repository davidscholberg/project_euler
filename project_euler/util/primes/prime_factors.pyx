from libcpp.list cimport list

# see sieve of eratosthenes
def prime_factors(long n) -> tuple[int]:
    cdef int potential_prime_factor = 2
    cdef list[int] factors
    while n > 1:
        if n % potential_prime_factor == 0:
            factors.push_back(potential_prime_factor)
            n //= potential_prime_factor
        else:
            potential_prime_factor += 1
    return tuple(factors)

# The only difference between this function and prime_factors is the type of
# the input. Using long is more flexible but slower.
def prime_factors_int(int n) -> tuple[int]:
    cdef int potential_prime_factor = 2
    cdef list[int] factors
    while n > 1:
        if n % potential_prime_factor == 0:
            factors.push_back(potential_prime_factor)
            n //= potential_prime_factor
        else:
            potential_prime_factor += 1
    return tuple(factors)