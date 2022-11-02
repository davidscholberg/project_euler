from project_euler.util.dates.month import days_in_month
from project_euler.util.dates.year import days_in_year

class Date:
    def __init__(self, year: int, month: int, day_of_month: int, day_of_week = None) -> None:
        self._year = year
        self._month = month - 1
        self._day_of_month = day_of_month
        self._day_of_week = day_of_week
        if day_of_week is None:
            self._calculate_day_of_week()

    def __eq__(self, __o: object) -> bool:
        return (
            self._year == __o._year and
            self._month == __o._month and
            self._day_of_month == __o._day_of_month
        )

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __lt__(self, __o: object) -> bool:
        if self._year < __o._year:
            return True
        if (
            self._year == __o._year and
            self._month < __o._month
        ):
            return True
        if (
            self._year == __o._year and
            self._month == __o._month and
            self._day_of_month < __o._day_of_month
        ):
            return True
        return False

    def __le__(self, __o: object) -> bool:
        return self.__lt__(__o) or self.__eq__(__o)

    def __gt__(self, __o: object) -> bool:
        return not self.__le__(__o)

    def __ge__(self, __o: object) -> bool:
        return self.__gt__(__o) or self.__eq__(__o)

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month + 1

    @property
    def day_of_month(self) -> int:
        return self._day_of_month

    @property
    def day_of_week(self) -> int:
        return self._day_of_week

    def _calculate_day_of_week(self) -> None:
        reference_date = Date(1900, 1, 1, day_of_week=1)
        days_between = self.days_to(reference_date)
        self._day_of_week = (reference_date.day_of_week - days_between) % 7

    def add_days(self, days: int) -> None:
        self._day_of_week = (self._day_of_week + days) % 7
        days_left = days
        while True:
            days_to_first_of_next_month = self.days_to_first_of_next_month()
            if days_left < days_to_first_of_next_month:
                break
            self._day_of_month = 1
            self._month += 1
            if self._month == 12:
                self._month = 0
                self._year += 1
            days_left -= days_to_first_of_next_month
        self._day_of_month += days_left

    def days_to_first_of_next_month(self) -> int:
        return days_in_month(self.month, self.year) - self.day_of_month + 1

    def days_to_first_of_next_year(self) -> int:
        return self.days_to_first_of_next_month() + sum(map(
            lambda month: days_in_month(month, self.year),
            range(self.month + 1, 13)
        ))

    def days_to(self, date: object) -> int:
        date1 = self
        date2 = date
        sign_factor = 1
        if date1 > date2:
            date1, date2 = date2, date1
            sign_factor = -1
        days = 0
        current_month = None
        current_day_of_month = None
        if date2.year > date1.year:
            days += date1.days_to_first_of_next_year()
            days += sum(map(
                days_in_year,
                range(date1.year + 1, date2.year)
            ))
            current_month = 1
            current_day_of_month = 1
        elif date2.month > date1.month:
            days += date1.days_to_first_of_next_month()
            current_month = date1.month + 1
            current_day_of_month = 1
        else:
            current_month = date1.month
            current_day_of_month = date1.day_of_month
        days += sum(map(
            lambda month: days_in_month(month, date2.year),
            range(current_month, date2.month)
        ))
        days += date2.day_of_month - current_day_of_month
        return days * sign_factor