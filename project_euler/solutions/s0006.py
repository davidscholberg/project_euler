def get_answer() -> int:
    square_of_sum = sum(range(1, 101)) ** 2
    sum_of_squares = sum(map(lambda n: n ** 2, range(1, 101)))
    return square_of_sum - sum_of_squares