from ..util.digits import GetDigitsIterator, get_number_of_digits

def get_phrase_for_number(n: int) -> tuple:
    words = ( \
        (None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"), \
        (None, ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"), "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"), \
        "hundred", \
        "thousand")
    if get_number_of_digits(n) == 1:
        return (words[0][n],)
    phrase = []
    power_of_ten = 0
    first_digit = -1
    for digit in GetDigitsIterator(n, reverse = True):
        if power_of_ten == 0:
            first_digit = digit
            if digit != 0:
                phrase = [words[power_of_ten][digit]]
        elif power_of_ten == 1:
            if digit == 1:
                phrase = [words[power_of_ten][digit][first_digit]]
            elif digit != 0:
                phrase = [words[power_of_ten][digit]] + phrase
        elif power_of_ten == 2:
            if digit != 0:
                hundreds_phrase = [words[0][digit], words[power_of_ten]]
                if len(phrase) > 0:
                    hundreds_phrase.append("and")
                phrase = hundreds_phrase + phrase
        elif power_of_ten == 3:
            if digit != 0:
                phrase = [words[0][digit], words[power_of_ten]] + phrase
        else:
            return ("number size not supported",)
        power_of_ten += 1
    return tuple(phrase)

class WordList:
    def __init__(self, from_file: str) -> None:
        self._list = []
        with open(from_file) as f:
            for line in f:
                self._list.extend(list(map(lambda s: s.strip("\""), line.split(","))))

    def sort(self, key = None, reverse = False) -> None:
        self._list.sort(key = key, reverse = reverse)

    def get_sum_of_word_scores(self) -> int:
        word_score_sum = 0
        for i, word in enumerate(self._list):
            word_uppercase = word.upper()
            word_score = sum(map(lambda c: ord(c) - 64, word_uppercase)) * (i + 1)
            word_score_sum += word_score
        return word_score_sum