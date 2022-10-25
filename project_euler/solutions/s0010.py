from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

def get_answer() -> int:
    return sum(sieve_of_eratosthenes(1999999))