from itertools import chain
from typing import Iterator

from project_euler.util.digits.digits import digits, number_from_digits
from project_euler.util.digits.pandigital import is_pandigital, max_pandigital, min_pandigital
from project_euler.util.sequences.permutations import permutations

def get_answer() -> int:
    def operand_splitters(digit_count: int) -> Iterator[int]:
        for splitter in range(1, (digit_count // 2) + 1):
            digit_count_a = splitter
            digit_count_b = digit_count - digit_count_a
            digit_count_c = 9 - digit_count_a - digit_count_b
            max_a = max_pandigital(digit_count_a)
            max_b = max_pandigital(digit_count_b)
            min_c = min_pandigital(digit_count_c)
            if max_a * max_b < min_c:
                continue
            min_a = min_pandigital(digit_count_a)
            min_b = min_pandigital(digit_count_b)
            max_c = max_pandigital(digit_count_c)
            if min_a * min_b > max_c:
                continue
            yield splitter
    product_set = set()
    for digit_count in range(2, 10):
        splitters = tuple(operand_splitters(digit_count))
        if len(splitters) == 0:
            continue
        candidate_digits = map(lambda t: tuple(map(lambda n: n + 1, t)), permutations(9, choose=digit_count))
        for permutation in candidate_digits:
            for splitter in splitters:
                a_digits = permutation[:splitter]
                b_digits = permutation[splitter:]
                c = number_from_digits(a_digits) * number_from_digits(b_digits)
                if is_pandigital(chain(a_digits, b_digits, digits(c))):
                    product_set.add(c)
    return sum(product_set)