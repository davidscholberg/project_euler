from ..util.sums import get_square_of_sum_of_range, get_sum_of_squares_in_range

def get_square_of_sum_minus_sum_of_squares_in_range(start: int, stop: int) -> int:
    return get_square_of_sum_of_range(start, stop) - get_sum_of_squares_in_range(start, stop)

def get_answer() -> int:
    return get_square_of_sum_minus_sum_of_squares_in_range(1, 100)