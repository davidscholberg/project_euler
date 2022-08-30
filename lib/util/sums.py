from .multiples import get_proper_divisors

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
