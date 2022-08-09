# This poorly written mess is essentially a rolling sieve of eritosthenes, where the sieve gets
# expanded by n numbers until the nth prime is found.
def get_nth_prime(n: int) -> int:
    marked_list = [True] * (n + 1)
    marked_list_index = 2
    current_prime_count = 1
    current_prime = 2
    while current_prime_count < n:
        while marked_list_index < len(marked_list):
            for prime_multiple in range(marked_list_index * 2, len(marked_list), marked_list_index):
                marked_list[prime_multiple] = False
            marked_list_index += 1
            while marked_list_index < len(marked_list):
                if marked_list[marked_list_index]:
                    current_prime = marked_list_index
                    current_prime_count += 1
                    if current_prime_count == n:
                        return current_prime
                    break
                marked_list_index += 1
        marked_list.extend([True] * n)
        for i in range(2, marked_list_index):
            if marked_list[i]:
                for prime_multiple in range((marked_list_index // i) * i, len(marked_list), i):
                    marked_list[prime_multiple] = False
        while marked_list_index < len(marked_list):
            if marked_list[marked_list_index]:
                current_prime = marked_list_index
                current_prime_count += 1
                if current_prime_count == n:
                    return current_prime
                break
            marked_list_index += 1
    return current_prime

# This function is unused but serves as a reference implementation.
def sieve_of_eritosthenes(n: int) -> list:
    marked_list = [True] * (n + 1)
    primes_list = [2]
    marked_list_index = 2
    while marked_list_index <= n:
        for prime_multiple in range(marked_list_index * 2, n + 1, marked_list_index):
            marked_list[prime_multiple] = False
        marked_list_index += 1
        while marked_list_index <= n:
            if marked_list[marked_list_index]:
                primes_list.append(marked_list_index)
                break
            marked_list_index += 1
    return primes_list

answer = get_nth_prime(10001)
print(answer)