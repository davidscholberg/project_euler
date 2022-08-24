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