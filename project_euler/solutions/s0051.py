from itertools import count, islice
from typing import Any, Iterable

from project_euler.util.digits.n_digit_number import max_n_digit_number
from project_euler.util.digits.repeating_digit_family import build_repeating_digit_family, get_repeating_digit_family_keys
from project_euler.util.primes.sieve_of_eratosthenes import RollingSieve

def filter_out_seen_keys(keys: Iterable[Any], seen_keys_dict: dict) -> tuple[Any]:
    """Return tuple of keys that don't exist in the given dict."""
    not_seen_keys = []
    for key in keys:
        if key not in seen_keys_dict:
            not_seen_keys.append(key)
    return tuple(not_seen_keys)

def get_answer() -> int:
    sieve = islice(RollingSieve(chunk_size=150000), 5, None)
    first_n_plus_1_digit_prime = 11
    for digit_count in count(start=2):
        largest_n_digit_number = max_n_digit_number(digit_count)
        n_digit_primes = set()
        n_digit_primes.add(first_n_plus_1_digit_prime)
        for prime in sieve:
            if prime > largest_n_digit_number:
                first_n_plus_1_digit_prime = prime
                break
            n_digit_primes.add(prime)
        prime_families = {}
        for prime in n_digit_primes:
            family_keys = get_repeating_digit_family_keys(prime)
            new_family_keys = filter_out_seen_keys(family_keys, prime_families)
            for key in new_family_keys:
                prime_family = tuple(filter(lambda n: n in n_digit_primes, build_repeating_digit_family(key)))
                if len(prime_family) == 8:
                    return min(prime_family)
                prime_families[key] = tuple(prime_family)