import imp
from itertools import chain

from project_euler.util.iterable.value_cap import value_cap
from project_euler.util.multiples.multiples import multiples

def get_answer() -> int:
    multiples_of_3 = value_cap(multiples(3), 999)
    multiples_of_5 = value_cap(multiples(5), 999)
    return sum(set(chain(multiples_of_3, multiples_of_5)))
