from ..util.project_paths import get_data_file_path
from ..util.words import WordList

def get_answer() -> int:
    word_list = WordList(get_data_file_path("list_of_names.txt"))
    word_list.sort()
    return word_list.get_sum_of_word_scores()