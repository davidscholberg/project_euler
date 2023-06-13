from project_euler.util.digits.lychrel_numbers import is_lychrel_number

def get_answer() -> int:
    non_lychrel_cache = set()
    lychrel_count = 0
    for n in range(10, 10000):
        if n in non_lychrel_cache:
            continue
        if is_lychrel_number(n, non_lychrel_cache):
            lychrel_count += 1
    return lychrel_count