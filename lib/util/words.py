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