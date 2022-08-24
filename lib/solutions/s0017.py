from lib.util.words import get_phrase_for_number

def get_answer() -> int:
    letter_count = 0
    for i in range(1, 1001):
        phrase = get_phrase_for_number(i)
        letter_count += sum(map(lambda word: len(word), phrase))
    return letter_count