from project_euler.util.digits.digits import digits
from project_euler.util.fractions.decimal_number import DecimalNumber

def divide(dividend: int, divisor: int) -> DecimalNumber:
    decimal_dividends = []
    dividend_digits = digits(dividend)
    current_dividend = next(dividend_digits)
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
        try:
            current_dividend += next(dividend_digits)
        except StopIteration:
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