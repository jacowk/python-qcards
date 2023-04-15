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
    def subtract_days(date, no_days):
        return date - datetime.timedelta(days=no_days)

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

    """
    A method to calculate the next view date for a weekly review stage
    Parameters:
    from_date: Represents the date you want to adjust
    weekday_cd: 0 = Monday, 1 = Tuesday, etc
    week_count: 1 means viewing a card once weekly. 2 means viewing a card every 2nd week.

    Jaco Koekemoer
    2023-04-11
    """
    @staticmethod
    def calculate_next_weekly_date(from_date, weekday_cd, week_count):
        # Calculate the no of days to add
        days_to_add = week_count * 7
        print("days_to_add = {:d}".format(days_to_add))

        # Add the days to the from_date
        adjusted_date = DateUtil.add_days(from_date, days_to_add)
        print("adjusted_date = {:%Y:%m:%d}".format(adjusted_date))

        # Get the week day for the adjusted date
        adjusted_weekday_cd = adjusted_date.isoweekday()

        """
        Adjust the date according to the weekday of the adjusted date and the weekday_cd.
        The adjusted date might be on a Tuesday, but the weekday_cd might be a Wednesday. In this case we need to 
        add 1 more day to the adjusted date. The opposite might be true also, in which case we need to subtract
        the required no of days to set the adjusted date to the intended week day.
        """
        if adjusted_weekday_cd < weekday_cd:
            day_adjustment = weekday_cd - adjusted_weekday_cd
            # Add the day difference
            adjusted_date = DateUtil.add_days(adjusted_date, day_adjustment)
        elif adjusted_weekday_cd > weekday_cd:
            day_adjustment = adjusted_weekday_cd - weekday_cd
            # Subtract the day difference
            adjusted_date = DateUtil.subtract_days(adjusted_date, day_adjustment)
        return adjusted_date

    """
    A method to calculate the next view date for a monthly review stage
    Parameters:
    from_date: Represents the date you want to adjust
    calendar_day: The day on which the view should be done, for example 1 to 31 of a month
    month_count: 1 means viewing a card monthly. 2 means viewing a card every 2nd month.
    
    Jaco Koekemoer
    2023-04-10
    """
    @staticmethod
    def calculate_next_monthly_date(from_date, calendar_day, month_count):
        current_year = from_date.year
        current_month = from_date.month
        adjusted_date = DateUtil.get_string_as_date(current_year, current_month, calendar_day)
        adjusted_date = DateUtil.add_months(adjusted_date, month_count)
        return adjusted_date
