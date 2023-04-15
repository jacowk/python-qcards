import unittest as ut
import review_stage_dao as rsd
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
        add_review_stage = rsd.AddReviewStage()
        add_review_stage.run(stack_id)

"""
A unit test for UpdateDailyReviewStage

Jaco Koekemoer
2023-04-15
"""
class UpdateDailyReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2

        update_review_stage = rsd.UpdateDailyReviewStage()
        update_review_stage.run(stack_id)

"""
A unit test for UpdateEverySecondDayReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateEverySecondDayReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        odd_even_cd = rsd.OddEven.ODD.value

        update_review_stage = rsd.UpdateEverySecondDayReviewStage()
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
        weekday_cd = rsd.Weekday.MONDAY.value
        week_count = 1 # Every week

        update_review_stage = rsd.UpdateWeeklyReviewStage()
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

        update_review_stage = rsd.UpdateMonthlyReviewStage()
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
        odd_even_cd = rsd.OddEven.ODD.value
        calculate_next_view_date = rsd.CalculateEverySecondDayNextViewDate()
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
        odd_even_cd = rsd.OddEven.EVEN.value
        calculate_next_view_date = rsd.CalculateEverySecondDayNextViewDate()
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
        calculate_next_view_date = rsd.CalculateWeeklyNextViewDate()
        next_view_date = calculate_next_view_date.run(weekday_cd, week_count)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        expected_date_string = "2023-04-24"
        ut.TestCase.assertTrue(expected_date_string, next_view_date_string)


"""
A unit test for CalculateMonthlyNextViewDate

Jaco Koekemoer
2023-04-10
"""
class CalculateMonthlyNextViewDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        calendar_day = 6
        month_count = 1
        calculate_next_view_date = rsd.CalculateMonthlyNextViewDate()
        next_view_date = calculate_next_view_date.run(calendar_day, month_count)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        expected_date_string = "2023-05-06"
        ut.TestCase.assertTrue(expected_date_string, next_view_date_string)


"""
A unit test for RetrieveReviewStageByStackId

Jaco Koekemoer
2023-04-15
"""
class RetrieveReviewStageByStackIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        retrieve_review_stage = rsd.RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage.run(stack_id)
        print(review_stage)


# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateDailyReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateEverySecondDayReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateWeeklyReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateMonthlyReviewStageTest)
# suite = loader.loadTestsFromTestCase(CalculateEverySecondDayNextViewDateWithOddTest)
# suite = loader.loadTestsFromTestCase(CalculateEverySecondDayNextViewDateWithEvenTest)
# suite = loader.loadTestsFromTestCase(CalculateWeeklyNextViewDateTest)
# suite = loader.loadTestsFromTestCase(CalculateMonthlyNextViewDateTest)
suite = loader.loadTestsFromTestCase(RetrieveReviewStageByStackIdTest)

runner = ut.TextTestRunner()
runner.run(suite)
