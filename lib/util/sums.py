from .multiples import get_proper_divisors

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