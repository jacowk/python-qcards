import datetime
from dateutil.relativedelta import relativedelta

"""
A general class for miscellaneous date utilities

Jaco Koekemoer
2023-04-04
"""
class DateUtil:

    """
    Functions required:
    add_one_week
    add_one_week_with_weekday
    add_two_weeks
    add_two_weeks_with_weekday
    calculate_next_odd_day
    calculate_next_even_day
    """
    @staticmethod
    def get_now_as_date():
        return datetime.date.today()

    @staticmethod
    def get_now_as_date_time():
        return datetime.datetime.now()

    @staticmethod
    def get_now_as_year_month_day():
        now = DateUtil.get_now_as_date_time()
        return now.strftime("%Y-%m-%d")

    @staticmethod
    def get_now_as_year_month_day_with_time():
        now = DateUtil.get_now_as_date_time()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_string_as_date(year, month, day):
        return datetime.date(int(year), int(month), int(day))

    @staticmethod
    def get_string_as_date_time(year, month, day, hour, minute, second):
        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

    @staticmethod
    def get_date_as_string(date):
        return date.strftime("%Y-%m-%d")

    @staticmethod
    def get_date_time_as_string(date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def add_days(date, no_days):
        return date + datetime.timedelta(days=no_days)

    @staticmethod
    def add_months(date, no_months):
        return date + relativedelta(months=no_months)

    """
    Calculate the next odd date after today
    from_date should be datetime.date()

    Jaco Koekemoer
    2023-04-08
    """
    @staticmethod
    def calculate_next_odd_date(from_date):
        odd_date_found = False
        next_view_date = from_date
        while odd_date_found == False:
            # Add 1 day to the date
            next_view_date = DateUtil.add_days(next_view_date, 1)
            next_view_day = next_view_date.day
            if DateUtil.validate_is_odd(next_view_day):
                odd_date_found = True
                break
        return next_view_date

    """
    A validation method to check if a given day value is on an odd day, e.g. 1, 3, 5, etc
    Jaco Koekemoer
    2023-04-09
    """
    @staticmethod
    def validate_is_odd(day_value):
        return day_value % 2 != 0

    """
    Calculate the next even date after today
    from_date should be datetime.date()

    Jaco Koekemoer
    2023-04-09
    """
    @staticmethod
    def calculate_next_even_date(from_date):
        even_date_found = False
        next_view_date = from_date
        while even_date_found == False:
            # Add 1 day to the date
            next_view_date = DateUtil.add_days(next_view_date, 1)
            next_view_day = next_view_date.day
            if DateUtil.validate_is_even(next_view_day):
                even_date_found = True
                break
        return next_view_date

    """
    A validation method to check if a given day value is on an even day, e.g. 2, 4, 6, etc
    Jaco Koekemoer
    2023-04-09
    """

    @staticmethod
    def validate_is_even(day_value):
        return day_value % 2 == 0