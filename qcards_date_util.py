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