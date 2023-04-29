from itertools import chain

from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes
from project_euler.util.sequences.permutations import permutations

def get_answer() -> int:
    four_digit_primes = filter(lambda p: p > 999, sieve_of_eratosthenes(9999))
    four_digit_prime_set = set(four_digit_primes)
    four_element_permutations = tuple(permutations(4))
    seen_primes = set(get_permuted_primes(1487, four_element_permutations, four_digit_prime_set))
    for prime in four_digit_prime_set:
        if prime in seen_primes:
            continue
        permuted_primes = get_permuted_primes(prime, four_element_permutations, four_digit_prime_set)
        permuted_primes_list = list(permuted_primes)
        for i in range(0, len(permuted_primes_list) - 1):
            for j in range(i + 1, len(permuted_primes_list)):
                prime_a = permuted_primes_list[i]
                prime_b = permuted_primes_list[j]
                difference = prime_b - prime_a
                next_candidate = prime_b + difference
                if next_candidate in permuted_primes:
                    return number_from_digits(chain(digits(prime_a), digits(prime_b), digits(next_candidate)))
        seen_primes.update(permuted_primes_list)
    return 0

def get_permuted_primes(n: int, permutations: tuple, prime_set: set) -> dict:
    """Get permutations of the given prime that are also prime and within the given prime set.

    We're returning a dict here because we need the fast lookup and also we want to preserve the key order"""
    permuted_primes_list = []
    prime_digits = digits(n)
    for permutation in permutations:
        permuted_number = number_from_digits(map(lambda i: prime_digits[i], permutation))
        if permuted_number in prime_set:
            permuted_primes_list.append(permuted_number)
    permuted_primes_list.sort()
    permuted_primes = {}
    for permuted_prime in permuted_primes_list:
        permuted_primes[permuted_prime] = True
    return permuted_primes