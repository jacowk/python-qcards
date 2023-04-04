import datetime

"""
A general class for miscellaneous date utilities

Jaco Koekemoer
2023-04-04
"""
class DateUtil:

    """
    Functions required:
    add_one_day
    add_one_month
    add_one_month_with_day
    add_one_week
    add_one_week_with_weekday
    add_two_weeks
    add_two_weeks_with_weekday
    calculate_next_odd_day
    calculate_next_even_day
    """

    def getNow(self):
        return datetime.datetime.now()

    def getNowAsYearMonthDay(self):
        now = self.getNow()
        return now.strftime("%Y-%m-%d")

    def getDateForYearMonthDay(self, year, month, day):
        return datetime.datetime(year, month, day)
