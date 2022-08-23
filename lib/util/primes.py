class SieveOfEritosthenesIterator:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__marked_list = [True] * (self.__limit + 1)
        self.__marked_list_index = -1

    @property
    def limit(self) -> int:
        return self.__limit

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__limit < 2:
            raise StopIteration
        if self.__marked_list_index == -1:
            self.__marked_list_index = 2
            return 2
        if self.__marked_list_index > self.__limit:
            raise StopIteration
        for prime_multiple in range(self.__marked_list_index * 2, self.__limit + 1, self.__marked_list_index):
            self.__marked_list[prime_multiple] = False
        self.__marked_list_index += 1
        while self.__marked_list_index <= self.__limit:
            if self.__marked_list[self.__marked_list_index]:
                return self.__marked_list_index
            self.__marked_list_index += 1
        raise StopIteration

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

# see sieve of eratosthenes
def get_prime_factors(n: int) -> list:
    prime_factors = []
    potential_prime_factor = 2
    while n > 1:
        if n % potential_prime_factor == 0:
            prime_factors.append(potential_prime_factor)
            n /= potential_prime_factor
        else:
            potential_prime_factor += 1
    return prime_factors

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