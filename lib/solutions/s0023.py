from ..util.sums import get_all_positive_integers_not_the_sum_of_two_abundant_numbers

def get_answer() -> int:
    return sum(get_all_positive_integers_not_the_sum_of_two_abundant_numbers())