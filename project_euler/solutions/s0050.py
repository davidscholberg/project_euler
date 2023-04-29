from project_euler.util.primes.sieve_of_eratosthenes import sieve_of_eratosthenes

def get_answer() -> int:
    primes = sieve_of_eratosthenes(999999)
    prime_dict = {}
    for prime in primes:
        prime_dict[prime] = 0
    prime_list = list(prime_dict)
    for i in range(len(prime_list) - 1):
        prime_sum = 0
        for j in range(i, len(prime_list)):
            prime_sum += prime_list[j]
            if prime_sum > 999999:
                break
            if prime_sum in prime_dict:
                current_run = j - i + 1
                if prime_dict[prime_sum] < current_run:
                    prime_dict[prime_sum] = current_run
    longest_run = 1
    longest_run_prime = 2
    for prime in prime_list:
        current_run = prime_dict[prime]
        if current_run > longest_run:
            longest_run = current_run
            longest_run_prime = prime
    return longest_run_prime