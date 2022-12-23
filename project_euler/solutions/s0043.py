from project_euler.util.digits.digits import number_from_digits
from project_euler.util.sequences.permutations import permutations

def get_answer() -> int:
    initial_primes = (2, 3, 5, 7, 11, 13, 17)
    partial_pandigitals = list(filter(
        lambda l: l[-1] % 2 == 0,
        map(list, permutations(10, choose=4))
    ))
    for i in range(1, len(initial_primes)):
        culled_partial_pandigitals = []
        for partial_pandigital in partial_pandigitals:
            present_digits_set = set(partial_pandigital)
            remaining_digits = filter(
                lambda digit: digit not in present_digits_set,
                range(0, 10)
            )
            for digit in remaining_digits:
                n = number_from_digits((partial_pandigital[-2], partial_pandigital[-1], digit))
                if n % initial_primes[i] == 0:
                    culled_partial_pandigitals.append(partial_pandigital + [digit])
        partial_pandigitals = culled_partial_pandigitals
    return sum(map(
        number_from_digits,
        partial_pandigitals
    ))