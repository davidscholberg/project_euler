from typing import Iterable

from project_euler.util.digits.concatenate import concatenate_integers
from project_euler.util.primes.is_prime import is_prime
from project_euler.util.primes.sieve_of_eratosthenes import RollingSieve

def concat_prime_pair_group_check(group: Iterable[int], candidate: int) -> bool:
    """Tells whether candidate belongs in the concat prime pair group."""
    for member in group:
        if not is_prime(concatenate_integers(candidate, member)):
            return False
        if not is_prime(concatenate_integers(member, candidate)):
            return False
    return True

def get_answer() -> int:
    sieve = RollingSieve(chunk_size=10000)
    concat_pairs_groups: list[list[int]] = []
    dangling_primes: list[int] = []
    for prime in sieve:
        if prime == 5:
            continue
        for concat_pairs_group in concat_pairs_groups:
            if concat_prime_pair_group_check(concat_pairs_group, prime):
                concat_pairs_group.append(prime)
                if len(concat_pairs_group) == 5:
                    return sum(concat_pairs_group)
        for dangling_prime in dangling_primes:
            if concat_prime_pair_group_check([prime], dangling_prime):
                concat_pairs_groups.append([dangling_prime, prime])
        dangling_primes.append(prime)
    return 0