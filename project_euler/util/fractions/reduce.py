def reduce_fraction(fraction: tuple[int, int]) -> tuple[int, int]:
    for i in range(min(fraction), 1, -1):
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            return reduce_fraction((fraction[0] // i, fraction[1] // i))
    return fraction