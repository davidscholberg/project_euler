from itertools import product, starmap

def get_answer() -> int:
    operand_pairs = product(range(2, 101), range(2, 101))
    powers = starmap(
        pow,
        operand_pairs
    )
    return len(set(powers))