from itertools import chain, count

from project_euler.util.digits.digits import digits
from project_euler.util.iterable.count_cap import count_cap

def get_answer() -> int:
    champernowne_segment = count_cap(1000000, chain.from_iterable(map(digits, count(1))))
    product = 1
    for i, digit in enumerate(champernowne_segment, start=1):
        if i in (1, 10, 100, 1000, 10000, 100000, 1000000):
            product *= digit
    return product