import unittest as ut
import category_dao as catd
import stack_dao as sd
import card_dao as cd
import review_stage_dao as rsd
import qcards_date_util as qdu

"""
A python script for testing a case end to end

Jaco Koekemoer
2023-04-15
"""
class AddCategoryTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test 3"
        parent_id = 2
        active = 1

        add_category = catd.AddCategory()
        add_category.run(description, parent_id, active)

class AddStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test Stack 2"
        active = 1
        source = "Testing different things 2"
        category_id = 3

        add_stack = sd.AddStack()
        add_stack.run(description, active, source, category_id)

class AddCardTest(ut.TestCase):

    @staticmethod
    def runTest():
        title = "Test title 2"
        front_content = "Test Front 2"
        back_content = "Test Front 2"
        stack_id = 5
        active = 1

        add_card = cd.AddCard()
        add_card.run(title, front_content, back_content, stack_id, active)

class AddReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        add_review_stage = rsd.AddReviewStage()
        add_review_stage.run(stack_id)

class RetrieveAllActiveCardsByStackIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        stack_id = 5

        # Run the test
        retrieve_cards = cd.RetrieveAllActiveCardsByStackId()
        results = retrieve_cards.run(stack_id)

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        for result in results:
            print(result)

class UpdateEverySecondDayReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        odd_even_cd = rsd.OddEven.ODD.value

        update_review_stage = rsd.UpdateEverySecondDayReviewStage()
        update_review_stage.run(stack_id, odd_even_cd)

class UpdateNextViewDateEverySecondDayTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        stack_id = 5

        # Retrieve the stack
        retrieve_review_stage = rsd.RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage.run(stack_id)
        odd_even_cd = review_stage[0][1]
        print("odd_even_cd = {}".format(odd_even_cd))

        # Calculate the next view date
        calculate_next_view_date = rsd.CalculateEverySecondDayNextViewDate()
        next_view_date = calculate_next_view_date.run(odd_even_cd)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        print("Calculated date: {:s}".format(next_view_date_string))

        # Update the next view date
        update_next_view_date = sd.UpdateNextViewDate()
        update_next_view_date.run(stack_id, next_view_date)

class UpdateWeeklyReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        weekday_cd = rsd.Weekday.MONDAY.value
        week_count = 1  # Every week

        update_review_stage = rsd.UpdateWeeklyReviewStage()
        update_review_stage.run(stack_id, weekday_cd, week_count)

class UpdateWeeklyNextViewDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        stack_id = 5

        # Retrieve the stack
        retrieve_review_stage = rsd.RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage.run(stack_id)

        weekday_cd = review_stage[0][2]
        week_count = review_stage[0][3]
        print("weekday_cd = {:d}".format(weekday_cd))
        print("week_count = {:d}".format(week_count))
        calculate_next_view_date = rsd.CalculateWeeklyNextViewDate()
        next_view_date = calculate_next_view_date.run(weekday_cd, week_count)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        print("Calculated date: {:s}".format(next_view_date_string))

        # Update the next view date
        update_next_view_date = sd.UpdateNextViewDate()
        update_next_view_date.run(stack_id, next_view_date)

class UpdateMonthlyReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5
        calendar_day = 6
        month_count = 1

        update_review_stage = rsd.UpdateMonthlyReviewStage()
        update_review_stage.run(stack_id, calendar_day, month_count)

class UpdateMonthlyNextViewDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        stack_id = 5

        # Retrieve the stack
        retrieve_review_stage = rsd.RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage.run(stack_id)

        calendar_day = review_stage[0][4]
        month_count = review_stage[0][5]
        calculate_next_view_date = rsd.CalculateMonthlyNextViewDate()
        next_view_date = calculate_next_view_date.run(calendar_day, month_count)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        print("Calculated date: {:s}".format(next_view_date_string))

        # Update the next view date
        update_next_view_date = sd.UpdateNextViewDate()
        update_next_view_date.run(stack_id, next_view_date)

class UpdateDailyReviewStageTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = 5

        update_review_stage = rsd.UpdateDailyReviewStage()
        update_review_stage.run(stack_id)

class RetrieveStacksForReviewTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = sd.RetrieveStacksForReview()
        result = retrieve_stacks.run()
        print(result)


# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddCategoryTest) # Add the category
# suite = loader.loadTestsFromTestCase(AddStackTest) # Add a stack for the category
# suite = loader.loadTestsFromTestCase(AddCardTest) # Add a card for the stack
# suite = loader.loadTestsFromTestCase(AddReviewStageTest) # Set the initial review stage to daily
# suite = loader.loadTestsFromTestCase(RetrieveAllActiveCardsByStackIdTest) # Retrieve all cards by stack id
# suite = loader.loadTestsFromTestCase(UpdateEverySecondDayReviewStageTest) # Update the review stage to every 2nd day
# suite = loader.loadTestsFromTestCase(UpdateNextViewDateEverySecondDayTest) # Update the next review date based on the review stage
# suite = loader.loadTestsFromTestCase(UpdateWeeklyReviewStageTest) # Update the review stage to weekly
# suite = loader.loadTestsFromTestCase(UpdateWeeklyNextViewDateTest) # Update the next review date based on the review stage
# suite = loader.loadTestsFromTestCase(UpdateMonthlyReviewStageTest) # Update the review stage to monthly
# suite = loader.loadTestsFromTestCase(UpdateMonthlyNextViewDateTest) # Update the next review date based on the review stage
# suite = loader.loadTestsFromTestCase(UpdateDailyReviewStageTest) # Update the review stage to daily
suite = loader.loadTestsFromTestCase(RetrieveStacksForReviewTest) # Retrieve all stacks to review today


runner = ut.TextTestRunner()
runner.run(suite)
