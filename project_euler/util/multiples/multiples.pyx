from libcpp.vector cimport vector
from typing import Iterable, Iterator

def multiples(n: int, minimum = None) -> Iterator[int]:
    if minimum is None:
        minimum = n
    current_multiple = minimum
    minimum_offset = n - (minimum % n)
    if minimum_offset < n:
        current_multiple += minimum_offset
    while True:
        yield current_multiple
        current_multiple += n

def smallest_number_divisible_by(numbers: Iterable[int]) -> int:
    sorted_numbers_list = sorted(numbers, reverse=True)
    cdef int largest_number = sorted_numbers_list.pop(0)
    cdef vector[int] sorted_numbers = sorted_numbers_list
    cdef int multiple = 0
    cdef int number = 0
    while True:
        multiple += largest_number
        found = True
        for number in sorted_numbers:
            if multiple % number != 0:
                found = False
                break
        if found:
            return multiple
    return 0