from typing import Iterable, Iterator

def multiples(n: int) -> Iterator[int]:
    current_multiple = n
    while True:
        yield current_multiple
        current_multiple += n

def smallest_number_divisible_by(numbers: Iterable[int]) -> int:
    sorted_numbers = sorted(numbers, reverse=True)
    largest_number = sorted_numbers[0]
    for multiple in multiples(largest_number):
        found = True
        for number in sorted_numbers:
            if multiple % number != 0:
                found = False
                break
        if found:
            return multiple