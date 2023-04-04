import unittest as ut
import qcards_date_util as qdu

"""
A unit test for DateUtil

Jaco Koekemoer
2023-04-04
"""
class DateUtilGetNowTest(ut.TestCase):

    def runTest(self):
        date_util = qdu.DateUtil()
        now = date_util.getNow()
        print(now)

"""
A unit test for DateUtil

Jaco Koekemoer
2023-04-04
"""
class DateUtilGetNowFormattedTest(ut.TestCase):

    def runTest(self):
        date_util = qdu.DateUtil()
        now = date_util.getNowAsYearMonthDay()
        print(now)

"""
A unit test for DateUtil

Jaco Koekemoer
2023-04-04
"""
class DateUtilGetDateForYearMonthDayTest(ut.TestCase):

    def runTest(self):
        year = 2023
        month = 3
        day = 4
        date_util = qdu.DateUtil()
        now = date_util.getDateForYearMonthDay(year, month, day)
        print(now)

# Run specific tests
loader = ut.TestLoader()
#suite = loader.loadTestsFromTestCase(DateUtilGetNowTest)
#suite = loader.loadTestsFromTestCase(DateUtilGetNowFormattedTest)
suite = loader.loadTestsFromTestCase(DateUtilGetDateForYearMonthDayTest)

runner = ut.TextTestRunner()
runner.run(suite)
