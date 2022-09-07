from .digits import GetDigitsIterator

class DecimalNumber:
    def __init__(self) -> None:
        self._digits = []
        self._decimal_point_index = -1
        self._repeating_digit_start = -1
        self._repeating_digit_end = -1

    @property
    def digits(self) -> tuple:
        return tuple(self._digits)

    @property
    def repeating_digits(self) -> tuple:
        if self._repeating_digit_start == -1:
            return tuple()
        return tuple(self._digits[self._repeating_digit_start:self._repeating_digit_end])

    def add_digit(self, digit: int) -> None:
        self._digits.append(digit)

    def decimal_point_is_set(self) -> bool:
        return self._decimal_point_index != -1

    def set_decimal_point(self) -> None:
        self._decimal_point_index = len(self._digits)

    def set_repeating_digit_indexes(self, start: int, end: int) -> None:
        self._repeating_digit_start = start + self._decimal_point_index
        self._repeating_digit_end = end + self._decimal_point_index

def divide(dividend: int, divisor: int) -> DecimalNumber:
    decimal_dividends = []
    dividend_digits = list(GetDigitsIterator(dividend))
    dividend_index = 0
    current_dividend = dividend_digits[0]
    result = DecimalNumber()
    done = False
    while not done:
        current_quotient = current_dividend // divisor
        result.add_digit(current_quotient)
        product = current_quotient * divisor
        difference = current_dividend - product
        if difference == 0:
            done = True
            continue
        current_dividend = difference * 10
        if dividend_index < len(dividend_digits) - 2:
            dividend_index += 1
            current_dividend += dividend_digits[dividend_index]
        else:
            if not result.decimal_point_is_set():
                result.set_decimal_point()
            for i, decimal_dividend in enumerate(decimal_dividends):
                if decimal_dividend == current_dividend:
                    result.set_repeating_digit_indexes(i, len(decimal_dividends))
                    done = True
                    break
            if not done:
                decimal_dividends.append(current_dividend)
    return result