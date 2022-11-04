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