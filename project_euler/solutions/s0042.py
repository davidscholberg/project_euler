from project_euler.paths import data_file_path
from project_euler.util.iterable.iter_len import iter_len
from project_euler.util.iterable.value_cap import value_cap
from project_euler.util.sequences.triangle_numbers import triangle_numbers
from project_euler.util.words.word_scores import word_value

def get_answer() -> int:
    with open(data_file_path('2000_english_words.txt')) as f:
        words = map(
            lambda s: s.strip('"'),
            f.read().split(',')
        )
        word_values = tuple(map(word_value, words))
        triangle_numbers_subset = set(value_cap(max(word_values), triangle_numbers()))
        return iter_len(filter(
            lambda word_value: word_value in triangle_numbers_subset,
            word_values
        ))