from typing import Iterator

from .digits import GetDigitsIterator
from .multiples import factorial, get_proper_divisors

class CombinationsOfNumbersThatSumToN:
    def __init__(self, number_list: tuple, n: int) -> None:
        self._combinations_iterator = self._get_all_combinations((), number_list, n)

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        return next(self._combinations_iterator)

    @classmethod
    def _get_all_combinations(cls, picked: tuple, available: tuple, n: int) -> Iterator[tuple]:
        sum_of_picked = sum(picked)
        if sum_of_picked > n:
            return
        if sum_of_picked == n:
            yield picked
            return
        if len(available) == 0:
            return
        first_number = available[0]
        new_available = tuple(filter(lambda e: e != first_number, available))
        for i in range(0, ((n - sum_of_picked) // first_number) + 1):
            new_picked = list(picked)
            new_picked.extend([first_number] * i)
            new_picked = tuple(new_picked)
            yield from cls._get_all_combinations(new_picked, new_available, n)

def get_all_abundant_numbers_under_n(n: int) -> tuple:
    abundant_numbers = []
    for i in range(1, n):
        if sum(get_proper_divisors(i)) > i:
            abundant_numbers.append(i)
    return tuple(abundant_numbers)

def get_all_sums_of_two_abundant_numbers_under_n(n: int) -> tuple:
    abundant_numbers = get_all_abundant_numbers_under_n(n)
    sums_of_two_abundant_numbers = []
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sums_of_two_abundant_numbers.append(abundant_numbers[i] + abundant_numbers[j])
    return tuple(sums_of_two_abundant_numbers)

def get_all_positive_integers_not_the_sum_of_two_abundant_numbers() -> tuple:
    abundant_number_sum_dict = {}
    for sum_of_two_abundant_numbers in get_all_sums_of_two_abundant_numbers_under_n(28124):
        if sum_of_two_abundant_numbers < 28124:
            abundant_number_sum_dict[sum_of_two_abundant_numbers] = True
    all_positive_integers_not_the_sum_of_two_abundant_numbers = []
    for i in range(1, 28124):
        if i not in abundant_number_sum_dict:
            all_positive_integers_not_the_sum_of_two_abundant_numbers.append(i)
    return tuple(all_positive_integers_not_the_sum_of_two_abundant_numbers)

def get_amicable_partner(n: int) -> int:
    candidate = sum(get_proper_divisors(n))
    if sum(get_proper_divisors(candidate)) == n and n != candidate:
        return candidate
    return 0

def get_square_of_sum_of_range(start: int, stop: int) -> int:
    return sum(range(start, stop + 1)) ** 2

def get_sum_of_squares_in_range(start: int, stop: int) -> int:
    return sum(map(lambda n: n ** 2, range(start, stop + 1)))

def get_sum_of_all_amicable_numbers_under_n(n: int) -> int:
    amicable_number_cache = {}
    running_sum = 0
    for i in range(1, n):
        if i in amicable_number_cache:
            continue
        candidate = get_amicable_partner(i)
        if candidate == 0 or candidate >= n:
            continue
        for amicable_number in (i, candidate):
            amicable_number_cache[amicable_number] = True
            running_sum += amicable_number
    return running_sum

def numbers_that_equal_sum_of_digit_factorials() -> Iterator[int]:
    digit_count = 2
    factorial_cache = {}
    def factorial_cache_checker(n: int) -> int:
        if n in factorial_cache:
            return factorial_cache[n]
        result = factorial(n)
        factorial_cache[n] = result
        return result
    sum_of_digit_factorials = lambda number: sum(map(lambda d: factorial_cache_checker(d), GetDigitsIterator(number)))
    while True:
        minimum_number = 10 ** (digit_count - 1)
        maximum_number = (10 ** digit_count) - 1
        if sum_of_digit_factorials(maximum_number) < minimum_number:
            break
        for i in range(minimum_number, maximum_number + 1):
            if i == sum_of_digit_factorials(i):
                yield i
        digit_count += 1

def numbers_that_equal_sum_of_nth_power_digits(n: int) -> Iterator[int]:
    digit_count = 2
    sum_of_nth_power_digits = lambda number: sum(map(lambda d: d ** n, GetDigitsIterator(number)))
    while True:
        minimum_number = 10 ** (digit_count - 1)
        maximum_number = (10 ** digit_count) - 1
        if sum_of_nth_power_digits(maximum_number) < minimum_number:
            break
        for i in range(minimum_number, maximum_number + 1):
            if i == sum_of_nth_power_digits(i):
                yield i
        digit_count += 1