from project_euler.util.iterable.value_cap import value_cap
from project_euler.util.sequences.fibonacci import fibonacci

def get_answer() -> int:
    return sum(filter(lambda n: n % 2 == 0, value_cap(4000000, fibonacci())))