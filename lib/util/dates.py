class Date:
    days_of_month = [
        None,
        31,
        lambda year: 29 if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

    def __init__(self, year: int, month: int, day: int, day_of_week: int = -1) -> None:
        self._year = year
        self._month = month
        self._day = day
        if not self._validate():
            raise ValueError("month and/or day out of range")
        if day_of_week == -1:
            reference_date = Date(1900, 1, 1, 1)
            reference_date.update_to(self._year, self._month, self._day)
            self._day_of_week = reference_date.day_of_week
        else:
            self._day_of_week = day_of_week

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    @property
    def day_of_week(self) -> int:
        return self._day_of_week

    def add_month(self) -> None:
        if self._month == 12:
            self.update_to(self._year + 1, 1, self._day)
        else:
            self.update_to(self._year, self._month + 1, self._day)

    def get_days_in_current_month(self) -> int:
        if self._month == 2:
            return Date.days_of_month[self._month](self._year)
        return Date.days_of_month[self._month]

    def is_in_future(self, year: int, month: int, day: int) -> bool:
        if year > self._year:
            return True
        elif year < self._year:
            return False
        if month > self._month:
            return True
        elif month < self._month:
            return False
        return day > self._day

    def is_in_past(self, year: int, month: int, day: int) -> bool:
        return not self.is_in_future(year, month, day) or not self.is_present(year, month, day)

    def is_present(self, year: int, month: int, day: int) -> bool:
        return year == self._year and month == self._month and day == self._day

    # TODO: make this work for dates in the past
    def update_to(self, to_year: int, to_month: int, to_day: int) -> None:
        days_added = 0
        while self.year < to_year or self.month < to_month:
            days_added += (self.get_days_in_current_month() - self._day) + 1
            self._day = 1
            self._month += 1
            if self._month > 12:
                self._month = 1
                self._year += 1
        days_added += to_day - self._day
        self._day = to_day
        self._day_of_week = (days_added + self._day_of_week) % 7

    def _validate(self) -> bool:
        if self._month < 1 or self._month > 12 or self._day < 1 or self._day > self.get_days_in_current_month():
            return False
        return True

def get_number_of_given_day_of_week_on_given_day_of_month_between(day_of_week: int, day_of_month: int, from_year: int, from_month: int, from_day: int, to_year: int, to_month: int, to_day: int) -> int:
    from_date = Date(from_year, from_month, from_day)
    if day_of_month < from_date.day:
        if from_date.month == 12:
            from_date.update_to(from_date.year + 1, 1, day_of_month)
        else:
            from_date.update_to(from_date.year, from_date.month + 1, day_of_month)
    elif day_of_month > from_date.day:
        from_date.update_to(from_date.year, from_date.month, day_of_month)
    day_count = 0
    while from_date.is_in_future(to_year, to_month, to_day) or from_date.is_present(to_year, to_month, to_day):
        if from_date.day_of_week == day_of_week:
            day_count += 1
        from_date.add_month()
    return day_count