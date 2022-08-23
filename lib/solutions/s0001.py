from ..util.multiples import get_list_of_multiples_capped

def get_answer() -> int:
    multiples_of_3 = get_list_of_multiples_capped(3, 1000)
    multiples_of_5 = get_list_of_multiples_capped(5, 1000)
    return sum(set(multiples_of_3 + multiples_of_5))