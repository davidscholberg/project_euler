import math

class GetDigitsIterator:
    def __init__(self, n: int, reverse: bool = False) -> None:
        self._n = n
        max_digit_power = math.floor(math.log(self._n, 10))
        if reverse:
            self._digit_power = 0
            self._digit_power_out_of_bounds = lambda x: x > max_digit_power
            self._digit_power_update_value = lambda x: x + 1
        else:
            self._digit_power = max_digit_power
            self._digit_power_out_of_bounds = lambda x: x < 0
            self._digit_power_update_value = lambda x: x - 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._digit_power_out_of_bounds(self._digit_power):
            raise StopIteration
        current_digit = (self._n // (10 ** self._digit_power)) % 10
        self._digit_power = self._digit_power_update_value(self._digit_power)
        return current_digit