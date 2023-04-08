import unittest as ut
import manage_review_stage as mrs

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

# Run specific tests
loader = ut.TestLoader()
suite = loader.loadTestsFromTestCase(AddReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateEverySecondDayReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateWeeklyReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateMonthlyReviewStageTest)

runner = ut.TextTestRunner()
runner.run(suite)
