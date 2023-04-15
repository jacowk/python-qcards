import unittest as ut
import qcards_date_util as qdu

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


"""
A unit test for the function validate_is_odd() in qcards_util.py

Jaco Koekemoer
2023-04-08
"""
class ValidateIsOddTest(ut.TestCase):

    @staticmethod
    def runTest():
        day_value = 13
        result = qdu.DateUtil().validate_is_odd(day_value)
        ut.TestCase.assertTrue(result, True)

"""
A unit test for the function calculate_next_odd_date() in qcards_util.py from today's date

Jaco Koekemoer
2023-04-08
"""
class CalculateNextOddDateFromTodayTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        today = qdu.DateUtil().get_now_as_date()

        # Test calculating the next odd date
        next_view_date = qdu.DateUtil().calculate_next_odd_date(today)

        print("From date: {:s}".format(qdu.DateUtil.get_date_as_string(today)))
        print("Next view date: {:s}".format(qdu.DateUtil.get_date_as_string(next_view_date)))

"""
A unit test for the function calculate_next_odd_date() in qcards_util.py using an odd date

Jaco Koekemoer
2023-04-09
"""
class CalculateNextOddDateFromOddDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        odd_date = qdu.DateUtil().get_string_as_date(2023, 4, 13)

        # Test calculating the next odd date
        next_view_date = qdu.DateUtil().calculate_next_odd_date(odd_date)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)

        # Assert results
        expected_date = "2023-04-13"
        ut.TestCase.assertTrue(expected_date, next_view_date_string)

"""
A unit test for the function calculate_next_odd_date() in qcards_util.py using an even date

Jaco Koekemoer
2023-04-09
"""
class CalculateNextOddDateFromEvenDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        odd_date = qdu.DateUtil().get_string_as_date(2023, 4, 12)

        # Test calculating the next odd date
        next_view_date = qdu.DateUtil().calculate_next_odd_date(odd_date)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)

        # Assert results
        expected_date = "2023-04-13"
        ut.TestCase.assertTrue(expected_date, next_view_date_string)

"""
A unit test for the function calculate_next_odd_date() in qcards_util.py using an even date

Jaco Koekemoer
2023-04-09
"""
class CalculateNextOddDateFromEndOfMonthTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        odd_date = qdu.DateUtil().get_string_as_date(2023, 3, 31)

        # Test calculating the next odd date
        next_view_date = qdu.DateUtil().calculate_next_odd_date(odd_date)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)

        # Assert results
        expected_date = "2023-04-01"
        ut.TestCase.assertTrue(expected_date, next_view_date_string)

"""
A unit test for the function validate_is_even() in qcards_util.py

Jaco Koekemoer
2023-04-08
"""
class ValidateIsEvenTest(ut.TestCase):

    @staticmethod
    def runTest():
        day_value = 14
        result = qdu.DateUtil().validate_is_even(day_value)
        ut.TestCase.assertTrue(result, True)

"""
A unit test for the function calculate_next_even_date() in qcards_util.py using an even date

Jaco Koekemoer
2023-04-09
"""
class CalculateNextEvenDateFromEvenDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        even_date = qdu.DateUtil().get_string_as_date(2023, 4, 14)

        # Test calculating the next even date
        next_view_date = qdu.DateUtil().calculate_next_even_date(even_date)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)

        # Assert results
        expected_date = "2023-04-16"
        ut.TestCase.assertTrue(expected_date, next_view_date_string)

"""
A unit test for the function calculate_next_even_date() in qcards_util.py using an odd date

Jaco Koekemoer
2023-04-09
"""
class CalculateNextEvenDateFromOddDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        odd_date = qdu.DateUtil().get_string_as_date(2023, 4, 13)

        # Test calculating the next odd date
        next_view_date = qdu.DateUtil().calculate_next_even_date(odd_date)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)

        # Assert results
        expected_date = "2023-04-14"
        ut.TestCase.assertTrue(expected_date, next_view_date_string)

"""
A unit test for the function calculate_next_even_date() in qcards_util.py using a date at the end of the month

Jaco Koekemoer
2023-04-09
"""
class CalculateNextEvenDateFromEndOfMonthTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Get today's date
        odd_date = qdu.DateUtil().get_string_as_date(2023, 3, 31)

        # Test calculating the next odd date
        next_view_date = qdu.DateUtil().calculate_next_even_date(odd_date)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)

        # Assert results
        expected_date = "2023-04-02"
        ut.TestCase.assertTrue(expected_date, next_view_date_string)

"""
A unit test for the calculate_next_weekly_date() function in the DateUtil class

Jaco Koekemoer
2023-04-11
"""
class CalculateNextWeeklyDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        from_date = qdu.DateUtil.get_now_as_date()
        weekday_cd = 0 # Monday
        week_count = 2

        # Run the test
        expected_view_date = "2024-04-24"
        next_view_date = qdu.DateUtil.calculate_next_weekly_date(from_date, weekday_cd, week_count)
        next_view_date_str = qdu.DateUtil.get_date_as_string(next_view_date)

        # Assert result
        ut.TestCase.assertTrue(next_view_date_str, expected_view_date)

"""
A unit test for the calculate_next_monthly_date() function in the DateUtil class

Jaco Koekemoer
2023-04-10
"""
class CalculateNextMonthlyDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        date1 = qdu.DateUtil.get_now_as_date()
        calendar_day = 20
        month_count = 9 # Every 2nd month
        expected_view_date = "2024-01-20"
        next_view_date = qdu.DateUtil.calculate_next_monthly_date(date1, calendar_day, month_count)
        next_view_date_str = qdu.DateUtil.get_date_as_string(next_view_date)
        ut.TestCase.assertTrue(next_view_date_str, expected_view_date)

        date2 = qdu.DateUtil.get_now_as_date()
        calendar_day = 20
        month_count = 1  # Every 2nd month
        expected_view_date = "2023-05-20"
        next_view_date = qdu.DateUtil.calculate_next_monthly_date(date2, calendar_day, month_count)
        next_view_date_str = qdu.DateUtil.get_date_as_string(next_view_date)
        ut.TestCase.assertTrue(next_view_date_str, expected_view_date)


# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(DateUtilGetNowTest)
# suite = loader.loadTestsFromTestCase(DateUtilGetNowAsYearMonthDayTest)
# suite = loader.loadTestsFromTestCase(DateUtilGetNowAsYearMonthDayWithTimeTest)
# suite = loader.loadTestsFromTestCase(DateUtilGetStringAsDateTest)
# suite = loader.loadTestsFromTestCase(DateUtilGetStringAsDateTimeTest)
# suite = loader.loadTestsFromTestCase(DateUtilGetDateAsStringTest)
# suite = loader.loadTestsFromTestCase(DateUtilGetDateTimeAsStringTest)
# suite = loader.loadTestsFromTestCase(DateUtilAddDaysTest)
# suite = loader.loadTestsFromTestCase(DateUtilAddMonthsTest)
# suite = loader.loadTestsFromTestCase(ValidateIsOddTest)
# suite = loader.loadTestsFromTestCase(CalculateNextOddDateFromTodayTest)
# suite = loader.loadTestsFromTestCase(CalculateNextOddDateFromOddDateTest)
# suite = loader.loadTestsFromTestCase(CalculateNextOddDateFromEvenDateTest)
# suite = loader.loadTestsFromTestCase(CalculateNextOddDateFromEndOfMonthTest)
# suite = loader.loadTestsFromTestCase(ValidateIsEvenTest)
# suite = loader.loadTestsFromTestCase(CalculateNextEvenDateFromEvenDateTest)
# suite = loader.loadTestsFromTestCase(CalculateNextEvenDateFromOddDateTest)
# suite = loader.loadTestsFromTestCase(CalculateNextEvenDateFromEndOfMonthTest)
suite = loader.loadTestsFromTestCase(CalculateNextWeeklyDateTest)
# suite = loader.loadTestsFromTestCase(CalculateNextMonthlyDateTest)

runner = ut.TextTestRunner()
runner.run(suite)
