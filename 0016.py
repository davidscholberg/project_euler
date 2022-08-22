from lib.get_digits import GetDigitsIterator

answer = sum(GetDigitsIterator(2 ** 1000))
print(answer)