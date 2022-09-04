from typing import Iterator

class Collatz:
    def __init__(self) -> None:
        self._sequence_length_cache = {}

    def get_number_of_collatz_terms(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n in self._sequence_length_cache:
            return self._sequence_length_cache[n]
        next_n = 0
        if n % 2 == 0:
            next_n = n // 2
        else:
            next_n = (3 * n) + 1
        collatz_term_count = self.get_number_of_collatz_terms(next_n) + 1
        self._sequence_length_cache[n] = collatz_term_count
        return collatz_term_count

class CollatzIterator:
    def __init__(self, n: int) -> None:
        self._current_value = n
        self._first_iteration = True

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._current_value == 1 and not self._first_iteration:
            raise StopIteration
        if self._first_iteration:
            self._first_iteration = False
            return self._current_value
        if self._current_value % 2 == 0:
            self._current_value //= 2
        else:
            self._current_value = (3 * self._current_value) + 1
        return self._current_value

class FibonacciIterator:
    def __init__(self, cap: int = 0) -> None:
        self._cap = cap
        self._previous_value = 1
        self._current_value = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._current_value == 0 or self._current_value == 1:
            self._current_value += 1
            if self._cap > 0 and self._current_value > self._cap:
                raise StopIteration
            return self._current_value
        new_value = self._current_value + self._previous_value
        if self._cap > 0 and new_value > self._cap:
            raise StopIteration
        self._previous_value = self._current_value
        self._current_value = new_value
        return new_value

class PermutationsIterator:
    def __init__(self, ordered_set: tuple, max_permutations: int = -1) -> None:
        self._max_permutations = max_permutations
        self._permutation_counter = 0
        self._permutation_generator = self._permute([], list(ordered_set))

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        if self._max_permutations != -1 and self._permutation_counter == self._max_permutations:
            raise StopIteration
        self._permutation_counter += 1
        return next(self._permutation_generator)

    @classmethod
    def _permute(cls, list_prefix: list, list_postfix: list) -> Iterator[tuple]:
        if not list_postfix:
            yield tuple(list_prefix)
            return
        for i in range(len(list_postfix)):
            new_list_prefix = list_prefix + [list_postfix[i]]
            new_list_postfix = list(filter(lambda e: e != list_postfix[i], list_postfix))
            yield from cls._permute(new_list_prefix, new_list_postfix)

class TriangleNumberIterator:
    def __init__(self, n: int = 0) -> None:
        self._limit = n
        self._previous_value = 0
        self._current_index = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._limit != 0 and self._current_index > self._limit:
            raise StopIteration
        current_value = self._previous_value + self._current_index
        self._previous_value = current_value
        self._current_index += 1
        return current_value

def get_nth_permutation(ordered_set: tuple, n: int) -> tuple:
    for i, permutation in enumerate(PermutationsIterator(ordered_set, n)):
        if i + 1 == n:
            return permutation
    return tuple()