from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.sums.sum_combinations import sum_combinations

def get_answer() -> int:
    return iter_len(sum_combinations(200, (1, 2, 5, 10, 20, 50, 100, 200)))