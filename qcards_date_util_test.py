import unittest as ut
import qcards_date_util as qdu
import datetime

"""
A unit test for DateUtil

Jaco Koekemoer
2023-04-04
"""


class DateUtilGetNowTest(ut.TestCase):

    @staticmethod
    def runTest():
        now = qdu.DateUtil.get_now_as_date_time()
        print(now)


class DateUtilGetNowAsYearMonthDayTest(ut.TestCase):

    @staticmethod
    def runTest():
        now = qdu.DateUtil.get_now_as_year_month_day()
        print(now)


class DateUtilGetNowAsYearMonthDayWithTimeTest(ut.TestCase):

    @staticmethod
    def runTest():
        now = qdu.DateUtil.get_now_as_year_month_day_with_time()
        print(now)


class DateUtilGetStringAsDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        year = "2022"
        month = "03"
        day = "1"
        result = qdu.DateUtil.get_string_as_date(year, month, day)
        print(type(result))
        print(result)


class DateUtilGetStringAsDateTimeTest(ut.TestCase):

    @staticmethod
    def runTest():
        year = "2022"
        month = "03"
        day = "1"
        hour = "10"
        minute = "23"
        second = "45"
        result = qdu.DateUtil.get_string_as_date_time(year, month, day, hour, minute, second)
        print(type(result))
        print(result)


class DateUtilGetDateAsStringTest(ut.TestCase):

    @staticmethod
    def runTest():
        year = "2022"
        month = "03"
        day = "1"
        input = qdu.DateUtil.get_string_as_date(year, month, day)
        result = qdu.DateUtil.get_date_as_string(input)
        print(type(result))
        print(result)


class DateUtilGetDateTimeAsStringTest(ut.TestCase):

    @staticmethod
    def runTest():
        year = "2022"
        month = "03"
        day = "1"
        hour = "10"
        minute = "23"
        second = "45"
        input = qdu.DateUtil.get_string_as_date_time(year, month, day, hour, minute, second)
        result = qdu.DateUtil.get_date_time_as_string(input)
        print(type(result))
        print(result)


class DateUtilAddDaysTest(ut.TestCase):

    @staticmethod
    def runTest():
        year = "2022"
        month = "03"
        day = "1"
        no_days = 3
        date = qdu.DateUtil.get_string_as_date(year, month, day)
        print("Before adding {:d} days".format(no_days))
        print(date)
        print(type(date))
        result = qdu.DateUtil.add_days(date, no_days)
        print("After adding days")
        print(type(result))
        print(result)


class DateUtilAddMonthsTest(ut.TestCase):

    @staticmethod
    def runTest():
        year = "2022"
        month = "03"
        day = "28"
        no_months = 3
        date = qdu.DateUtil.get_string_as_date(year, month, day)
        print("Before adding {:d} months".format(no_months))
        print(date)
        result = qdu.DateUtil.add_months(date, no_months)
        print("After adding months")
        print(type(result))
        print(result)

# Run specific tests
loader = ut.TestLoader()
#suite = loader.loadTestsFromTestCase(DateUtilGetNowTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetNowAsYearMonthDayTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetNowAsYearMonthDayWithTimeTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetStringAsDateTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetStringAsDateTimeTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetDateAsStringTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetDateTimeAsStringTest)
suite = loader.loadTestsFromTestCase(DateUtilAddDaysTest)
#suite = loader.loadTestsFromTestCase(DateUtilAddMonthsTest)

runner = ut.TextTestRunner()
runner.run(suite)
