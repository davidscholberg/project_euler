from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.primes.is_prime import is_prime
from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

def get_answer() -> int:
    total = 0
    for prime in sieve_of_eratosthenes(739397):
        if prime < 10:
            continue
        digits_tuple = digits(prime)
        truncatable = True
        for i, digit in enumerate(digits_tuple):
            if (digit % 2 == 0 and (digit != 2 or i != 0)) or (digit == 5 and i != 0):
                truncatable = False
                break
        if not truncatable:
            continue
        for i in range(0, len(digits_tuple)):
            if not is_prime(number_from_digits(digits_tuple[i:])):
                truncatable = False
                break
        if not truncatable:
            continue
        for i in range(len(digits_tuple), 0, -1):
            if not is_prime(number_from_digits(digits_tuple[:i])):
                truncatable = False
                break
        if not truncatable:
            continue
        total += prime
    return total