from project_euler.util.fractions.divide import divide

def get_answer() -> int:
    return max(
        map(
            lambda n: (n, len(divide(1, n).repeating_digits)),
            range(2, 1000)
        ),
        key=lambda t: t[1]
    )[0]