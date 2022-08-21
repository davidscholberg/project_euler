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

def get_number_of_collatz_terms(n: int) -> int:
    count = 0
    for i in CollatzIterator(n):
        count += 1
    return count

def get_number_with_max_number_of_collatz_terms_in_range(start: int, end: int) -> int:
    max_collatz_terms = 0
    max_collatz_terms_number = 0
    for i in range(start, end + 1):
        collatz_terms = get_number_of_collatz_terms(i)
        if collatz_terms > max_collatz_terms:
            max_collatz_terms = collatz_terms
            max_collatz_terms_number = i
    return max_collatz_terms_number

answer = get_number_with_max_number_of_collatz_terms_in_range(1, 999999)
print(answer)