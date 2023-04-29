from project_euler.util.digits.truncate import left_truncate

def get_answer() -> int:
    total = 0
    for n in range(1, 1001):
        if n % 10 == 0:
            continue
        power = n
        for _ in range(1, n):
            power *= n
            power = left_truncate(power, to=10)
        total += power
        total = left_truncate(total, to=10)
    return total