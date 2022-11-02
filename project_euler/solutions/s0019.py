from project_euler.util.dates.date import Date

def get_answer() -> int:
    date = Date(1901, 1, 1)
    end_date = Date(2000, 12, 31)
    sundays_on_first_of_month = 0
    while date <= end_date:
        if date.day_of_week == 0:
            sundays_on_first_of_month += 1
        date.add_days(date.days_to_first_of_next_month())
    return sundays_on_first_of_month