from itertools import chain

from project_euler.util.iterable.count import count
from project_euler.util.words.number_words import number_words

def get_answer() -> int:
    all_number_words = chain.from_iterable(map(number_words, range(1, 1001)))
    return count(filter(lambda c: c != ' ', all_number_words))