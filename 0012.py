import math

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

def get_factors(n: int) -> tuple:
    factors = [1]
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    if n > 1:
        factors.append(n)
    return tuple(factors)

def get_first_triangle_number_with_over_n_divisors(n: int) -> int:
    for triangle_number in TriangleNumberIterator():
        if len(get_factors(triangle_number)) > n:
            return triangle_number

answer = get_first_triangle_number_with_over_n_divisors(500)
print(answer)