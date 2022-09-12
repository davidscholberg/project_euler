from ..util.digits import get_number_from_digits, is_pandigital
from ..util.sequences import PermutationsIterator

def get_answer() -> int:
    set_of_products = set()
    for digit_count in range(2, 9):
        viable_splitters = get_viable_splitters(digit_count)
        if not viable_splitters:
            continue
        for permutation in PermutationsIterator((1, 2, 3, 4, 5, 6, 7, 8, 9), choose_k=digit_count):
            for splitter in viable_splitters:
                a = get_number_from_digits(permutation[:splitter])
                b = get_number_from_digits(permutation[splitter:])
                c = a * b
                if is_pandigital((a, b, c)):
                    set_of_products.add(c)
    return sum(set_of_products)

def get_viable_splitters(digit_count: int) -> bool:
    splitters = []
    for splitter in range(1, (digit_count // 2) + 1):
        digit_count_a = splitter
        digit_count_b = digit_count - digit_count_a
        digit_count_c = 9 - digit_count_a - digit_count_b
        max_a = get_number_from_digits([9] * digit_count_a)
        max_b = get_number_from_digits([9] * digit_count_b)
        min_c = get_number_from_digits([1] * digit_count_c)
        if max_a * max_b < min_c:
            continue
        min_a = get_number_from_digits([1] * digit_count_a)
        min_b = get_number_from_digits([1] * digit_count_b)
        max_c = get_number_from_digits([9] * digit_count_c)
        if min_a * min_b > max_c:
            continue
        splitters.append(splitter)
    return splitters