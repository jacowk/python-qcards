import unittest as ut
import review_stage_dao as rsd

"""
A unit test for AddReviewStage

Jaco Koekemoer
2023-04-08
"""
class AddReviewStageDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        add_review_stage = rsd.AddReviewStageDAO()
        add_review_stage.run(stack_id)

"""
A unit test for UpdateDailyReviewStage

Jaco Koekemoer
2023-04-15
"""
class UpdateDailyReviewStageDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2

        update_review_stage = rsd.UpdateDailyReviewStageDAO()
        update_review_stage.run(stack_id)

"""
A unit test for UpdateEverySecondDayReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateEverySecondDayReviewStageDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        odd_even_cd = rsd.OddEven.ODD.value

        update_review_stage = rsd.UpdateEverySecondDayReviewStageDAO()
        update_review_stage.run(stack_id, odd_even_cd)

"""
A unit test for UpdateWeeklyReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateWeeklyReviewStageDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        weekday_cd = rsd.Weekday.MONDAY.value
        week_count = 1 # Every week

        update_review_stage = rsd.UpdateWeeklyReviewStageDAO()
        update_review_stage.run(stack_id, weekday_cd, week_count)

"""
A unit test for UpdateMonthlyReviewStage

Jaco Koekemoer
2023-04-08
"""
class UpdateMonthlyReviewStageDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 2
        calendar_day = 6
        month_count = 1

        update_review_stage = rsd.UpdateMonthlyReviewStageDAO()
        update_review_stage.run(stack_id, calendar_day, month_count)

"""
A unit test for RetrieveReviewStageByStackId

Jaco Koekemoer
2023-04-15
"""
class RetrieveReviewStageByStackIdDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        retrieve_review_stage = rsd.RetrieveReviewStageByStackIdDAO()
        review_stage = retrieve_review_stage.run(stack_id)
        print(review_stage)


# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateDailyReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateEverySecondDayReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateWeeklyReviewStageTest)
# suite = loader.loadTestsFromTestCase(UpdateMonthlyReviewStageTest)
suite = loader.loadTestsFromTestCase(RetrieveReviewStageByStackIdDAOTest)

runner = ut.TextTestRunner()
runner.run(suite)
