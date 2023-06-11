from project_euler.util.combinatorics.n_choose_k import n_choose_k

def get_answer() -> int:
    total = 0
    for n in range(23, 101):
        lower_bound = 0
        for k in range(1, n + 1):
            if n_choose_k(n, k) > 1000000:
                lower_bound = k
                break
        upper_bound = 0
        for k in range(n, 0, -1):
            if n_choose_k(n, k) > 1000000:
                upper_bound = k
                break
        total += upper_bound - lower_bound + 1
    return total