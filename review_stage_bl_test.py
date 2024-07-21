import unittest as ut
import review_stage_bl as rsbl
import review_stage_constant as rsc
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

        review_stage = rsbl.ReviewStage()
        review_stage.set_stack_id(stack_id)

        add_review_stage = rsbl.AddReviewStage()
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

        review_stage = rsbl.ReviewStage()
        review_stage.set_stack_id(stack_id)

        update_review_stage = rsbl.UpdateDailyReviewStage()
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
        odd_even_cd = rsc.OddEven.ODD.value

        review_stage = rsbl.ReviewStage()
        review_stage.set_stack_id(stack_id)
        review_stage.set_odd_even_cd(odd_even_cd)

        update_review_stage = rsbl.UpdateEverySecondDayReviewStage()
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
        weekday_cd = rsc.Weekday.MONDAY.value
        week_count = 1 # Every week

        review_stage = rsbl.ReviewStage()
        review_stage.set_stack_id(stack_id)
        review_stage.set_weekday_cd(weekday_cd)
        review_stage.set_month_count(week_count)

        update_review_stage = rsbl.UpdateWeeklyReviewStage()
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

        review_stage = rsbl.ReviewStage()
        review_stage.set_stack_id(stack_id)
        review_stage.set_calendar_day(calendar_day)
        review_stage.set_month_count(month_count)

        update_review_stage = rsbl.UpdateMonthlyReviewStage()
        update_review_stage.run(review_stage)

"""
A unit test for RetrieveReviewStageByStackId

Jaco Koekemoer
2023-04-15
"""
class RetrieveReviewStageByStackIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        retrieve_review_stage = rsbl.RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage.run(stack_id)
        print(review_stage)

"""
A unit test for CalculateEverySecondDayNextViewDate

Jaco Koekemoer
2023-04-10
"""
class CalculateEverySecondDayNextViewDateWithOddTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 1
        odd_even_cd = rsc.OddEven.ODD.value
        calculate_next_view_date = rsbl.CalculateEverySecondDayNextViewDate()
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
        odd_even_cd = rsc.OddEven.EVEN.value
        calculate_next_view_date = rsbl.CalculateEverySecondDayNextViewDate()
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
        calculate_next_view_date = rsbl.CalculateWeeklyNextViewDate()
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
        calculate_next_view_date = rsbl.CalculateMonthlyNextViewDate()
        next_view_date = calculate_next_view_date.run(calendar_day, month_count)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        expected_date_string = "2023-05-06"
        ut.TestCase.assertTrue(expected_date_string, next_view_date_string)

"""
A unit test for CalculateMonthlyNextViewDate

Jaco Koekemoer
2023-04-10
"""
class ReviewStageLookupDictTest(ut.TestCase):

    @staticmethod
    def runTest():
        review_stage_lookup_dict = rsbl.ReviewStageLookupDict()
        review_stage_dict = review_stage_lookup_dict.run()
        print(review_stage_dict)

"""
A unit test for OddEvenLookupDict

Jaco Koekemoer
2023-04-10
"""
class OddEvenLookupDictTest(ut.TestCase):

    @staticmethod
    def runTest():
        odd_even_lookup_dict = rsbl.OddEvenLookupDict()
        odd_even_dict = odd_even_lookup_dict.run()
        print(odd_even_dict)

"""
A unit test for WeekdayLookupDict

Jaco Koekemoer
2023-04-10
"""
class WeekdayLookupDictTest(ut.TestCase):

    @staticmethod
    def runTest():
        weekday_lookup_dict = rsbl.WeekdayLookupDict()
        weekday_dict = weekday_lookup_dict.run()
        print(weekday_dict)

"""
A unit test for SetupInitialReviewStage

Jaco Koekemoer
2023-05-05
"""
class SetupInitialReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 3
        setup_review_stage = rsbl.SetupInitialReviewStage()
        setup_review_stage.run(stack_id)



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
# suite = loader.loadTestsFromTestCase(RetrieveReviewStageByStackIdTest)
# suite = loader.loadTestsFromTestCase(ReviewStageLookupDictTest)
# suite = loader.loadTestsFromTestCase(OddEvenLookupDictTest)
# suite = loader.loadTestsFromTestCase(WeekdayLookupDictTest)
suite = loader.loadTestsFromTestCase(SetupInitialReviewStageTest)

runner = ut.TextTestRunner()
runner.run(suite)
