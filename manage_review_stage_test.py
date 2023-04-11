import unittest as ut
import manage_review_stage as mrs
import qcards_date_util as qdu

"""
A unit test for AddReviewStage

Jaco Koekemoer
2023-04-08
"""
class AddReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        add_review_stage = mrs.AddReviewStage()
        add_review_stage.run(stack_id)

"""
A unit test for UpdateEverySecondDayReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateEverySecondDayReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        odd_even_cd = mrs.OddEven.ODD.value

        update_review_stage = mrs.UpdateEverySecondDayReviewStage()
        update_review_stage.run(stack_id, odd_even_cd)

"""
A unit test for UpdateWeeklyReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateWeeklyReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        weekday_cd = mrs.Weekday.MONDAY.value
        week_count = 1 # Every week

        update_review_stage = mrs.UpdateWeeklyReviewStage()
        update_review_stage.run(stack_id, weekday_cd, week_count)

"""
A unit test for UpdateMonthlyReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateMonthlyReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        calendar_day = 6
        month_count = 1

        update_review_stage = mrs.UpdateMonthlyReviewStage()
        update_review_stage.run(stack_id, calendar_day, month_count)

"""
A unit test for CalculateEverySecondDayNextViewDate

Jaco Koekemoer
2023-04-10
"""
class CalculateEverySecondDayNextViewDateWithOddTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 1
        odd_even_cd = mrs.OddEven.ODD.value
        calculate_next_view_date = mrs.CalculateEverySecondDayNextViewDate()
        next_view_date = calculate_next_view_date.run(stack_id, odd_even_cd)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        expected_date_string = "2023-04-11"
        ut.TestCase.assertTrue(expected_date_string, next_view_date_string)

"""
A unit test for CalculateEverySecondDayNextViewDate

Jaco Koekemoer
2023-04-10
"""
class CalculateEverySecondDayNextViewDateWithEvenTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 1
        odd_even_cd = mrs.OddEven.EVEN.value
        calculate_next_view_date = mrs.CalculateEverySecondDayNextViewDate()
        next_view_date = calculate_next_view_date.run(stack_id, odd_even_cd)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        expected_date_string = "2023-04-12"
        ut.TestCase.assertTrue(expected_date_string, next_view_date_string)


"""
A unit test for CalculateWeeklyNextViewDate

Jaco Koekemoer
2023-04-10
"""
class CalculateWeeklyNextViewDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        weekday_cd = 0  # Monday
        week_count = 2
        calculate_next_view_date = mrs.CalculateWeeklyNextViewDate()
        next_view_date = calculate_next_view_date.run(weekday_cd, week_count)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        expected_date_string = "2023-04-24"
        ut.TestCase.assertTrue(expected_date_string, next_view_date_string)


# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateEverySecondDayReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateWeeklyReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateMonthlyReviewStageTest)
# suite = loader.loadTestsFromTestCase(CalculateEverySecondDayNextViewDateWithOddTest)
# suite = loader.loadTestsFromTestCase(CalculateEverySecondDayNextViewDateWithEvenTest)
suite = loader.loadTestsFromTestCase(CalculateWeeklyNextViewDateTest)

runner = ut.TextTestRunner()
runner.run(suite)
