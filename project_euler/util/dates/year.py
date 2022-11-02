def days_in_year(year: int) -> int:
    return 366 if is_leap_year(year) else 365

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False