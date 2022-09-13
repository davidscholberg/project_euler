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
        if len(self._digits) == 1 and self._digits[0] == 0 and self._decimal_point_index == -1 and digit == 0:
            return
        self._digits.append(digit)

    def decimal_point_is_set(self) -> bool:
        return self._decimal_point_index != -1

    def set_decimal_point(self) -> None:
        self._decimal_point_index = len(self._digits)

    def set_repeating_digit_indexes(self, start: int, end: int) -> None:
        self._repeating_digit_start = start + self._decimal_point_index
        self._repeating_digit_end = end + self._decimal_point_index

    def __eq__(self, __o: object) -> bool:
        if self._repeating_digit_start != __o._repeating_digit_start:
            return False
        if self._repeating_digit_end != __o._repeating_digit_end:
            return False
        if self._decimal_point_index != __o._decimal_point_index:
            return False
        if len(self._digits) != len(__o._digits):
            return False
        for i in range(len(self._digits)):
            if self._digits[i] != __o._digits[i]:
                return False
        return True

    def __str__(self) -> str:
        number_list = list(self._digits)
        if self._decimal_point_index != -1:
            if self._repeating_digit_start != -1:
                number_list[self._repeating_digit_end:self._repeating_digit_end] = ")"
                number_list[self._repeating_digit_start:self._repeating_digit_start] = "("
            number_list[self._decimal_point_index:self._decimal_point_index] = "."
        return "".join(map(str, number_list))

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
        if dividend_index < len(dividend_digits) - 1:
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

def multiply_fractions(fraction_a: tuple, fraction_b: tuple) -> tuple:
    return tuple(map(lambda a, b: a * b, fraction_a, fraction_b))

def reduce_fraction(fraction: tuple) -> tuple:
    for i in range(min(fraction), 1, -1):
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            return reduce_fraction(tuple(map(lambda n: n // i, fraction)))
    return fraction
