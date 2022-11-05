from itertools import chain

from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.words.number_words import number_words

def get_answer() -> int:
    all_number_words = chain.from_iterable(map(number_words, range(1, 1001)))
    return iter_len(filter(lambda c: c != ' ', all_number_words))