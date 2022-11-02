from typing import Iterable, Iterator

from project_euler.util.dates.year import is_leap_year

def days_in_month(month:int, year: int) -> int:
    month -= 1
    match month:
        case 0:
            return 31
        case 1:
            return 29 if is_leap_year(year) else 28
        case 2:
            return 31
        case 3:
            return 30
        case 4:
            return 31
        case 5:
            return 30
        case 6:
            return 31
        case 7:
            return 31
        case 8:
            return 30
        case 9:
            return 31
        case 10:
            return 30
        case 11:
            return 31