from itertools import count

from project_euler.util.grids.spiral import spiral_diagonals
from project_euler.util.primes.is_prime import is_prime

def get_answer() -> int:
    prime_diagonal_count = 0
    non_prime_diagonal_count = 1
    for layer in count(2):
        diagonals = spiral_diagonals(layer)
        for i in range(len(diagonals) - 1):
            if is_prime(diagonals[i]):
                prime_diagonal_count += 1
            else:
                non_prime_diagonal_count += 1
        non_prime_diagonal_count += 1
        if prime_diagonal_count * 10 < prime_diagonal_count + non_prime_diagonal_count:
            return (layer * 2) - 1
    return 0