from typing import Iterator

from project_euler.util.iterable.value_cap import value_cap
from project_euler.util.multiples.multiples import multiples

def sieve_of_eratosthenes(limit: int) -> Iterator[int]:
    composites = [False] * (limit + 2)
    current_prime = 2
    while current_prime <= limit:
        yield current_prime
        for multiple in value_cap(limit, multiples(current_prime, minimum=current_prime * 2)):
            composites[multiple] = True
        current_prime += 1
        while composites[current_prime]:
            current_prime += 1

class RollingSieve:
    def __init__(self, chunk_size: int = 10000) -> None:
        self._chunk_size = chunk_size
        self._limit = self._chunk_size
        self._composites = [False] * (self._chunk_size + 1)
        self.seen_primes = []
        self._current_prime = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_prime == 0:
            self._current_prime = 2
            self.seen_primes.append(self._current_prime)
            return self._current_prime
        self._set_composites(self._current_prime, self._current_prime * 2)
        prime_candidate = self._current_prime + 1
        while True:
            if prime_candidate > self._limit:
                self._extend_limit()
                continue
            if self._is_composite(prime_candidate):
                prime_candidate += 1
                continue
            self._current_prime = prime_candidate
            self.seen_primes.append(self._current_prime)
            return self._current_prime

    def _extend_limit(self) -> None:
        minimum_composite = self._limit + 1
        self._limit += self._chunk_size
        self._composites = [False] * (self._chunk_size + 1)
        for seen_prime in self.seen_primes:
            self._set_composites(seen_prime, minimum_composite)

    def _is_composite(self, n: int) -> bool:
        return self._composites[n % self._chunk_size]

    def _set_composite(self, n: int) -> None:
        self._composites[n % self._chunk_size] = True

    def _set_composites(self, prime: int, minimum_composite: int) -> None:
        for multiple in value_cap(self._limit, multiples(prime, minimum=minimum_composite)):
            self._set_composite(multiple)

    def update_to(self, n: int) -> None:
        if n <= self._current_prime:
            return
        while self.__next__() < n:
            pass