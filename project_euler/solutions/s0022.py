from project_euler.paths import data_file_path
from project_euler.util.words.word_scores import word_scores

def get_answer() -> int:
    with open(data_file_path('names.txt')) as f:
        names = map(
            lambda s: s.strip('"'),
            f.read().split(',')
        )
        return sum(word_scores(names))