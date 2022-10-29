from collections import deque

from project_euler.util.digits.digits import digits

ones = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
)

ten_to_nineteen = (
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
)

tens = (
    None,
    None,
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
)

power_suffix = (
    None,
    None,
    'hundred',
    'thousand',
)

def number_words(n: int) -> str:
    words = deque()
    ones_digit = None
    for power, digit in enumerate(digits(n, reverse=True)):
        if power == 0:
            words.appendleft(ones[digit])
            ones_digit = digit
        elif power == 1:
            if digit == 1 or words[0] == 'zero':
                words.popleft()
            if digit == 1:
                words.appendleft(ten_to_nineteen[ones_digit])
            elif digit > 1:
                words.appendleft(tens[digit])
        else:
            if power == 2 and len(words) != 0:
                words.appendleft('and')
            if digit > 0:
                words.appendleft(power_suffix[power])
                words.appendleft(ones[digit])
    return ' '.join(words)