from project_euler.util.digits.digits import number_from_digits
from project_euler.util.primes.is_prime import is_prime
from project_euler.util.sequences.permutations import permutations

def get_answer() -> int:
    max_pandigital_prime = 0
    for digit_count in range(2, 10):
        for digits in permutations(digit_count):
            pandigital = number_from_digits(map(lambda n: n + 1, digits))
            if is_prime(pandigital):
                max_pandigital_prime = pandigital
    return max_pandigital_prime