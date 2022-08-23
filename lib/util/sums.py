def get_square_of_sum_of_range(start: int, stop: int) -> int:
    return sum(range(start, stop + 1)) ** 2

def get_sum_of_squares_in_range(start: int, stop: int) -> int:
    return sum(map(lambda n: n ** 2, range(start, stop + 1)))