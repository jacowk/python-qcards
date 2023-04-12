import unittest as ut
import manage_stacks as ms
import qcards_date_util as qdu
import manage_review_stage as mrs

"""
A class to test AddStack

Jaco Koekemoer
2023-04-07
"""
class AddStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test Stack"
        active = 1
        source = "Testing different things"
        category_id = 2

        add_stack = ms.AddStack()
        add_stack.run(description, active, source, category_id)

"""
A class to test UpdateStack

Jaco Koekemoer
2023-04-07
"""
class UpdateStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 1
        description = "Java Lang Package"
        active = 1
        source = "www.oracle.com"
        category_id = 1
        last_view_date = qdu.DateUtil.get_now_as_date_time()
        today = qdu.DateUtil.get_now_as_date()
        next_view_date = qdu.DateUtil.add_days(today, 2)

        update_stack = ms.UpdateStack()
        update_stack.run(id, description, active, source, category_id, last_view_date, next_view_date)

"""
A class to test UpdateNextViewDate

Jaco Koekemoer
2023-04-07
"""
class UpdateNextViewDateTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        stack_id = 4
        odd_even_cd = mrs.OddEven.ODD.value

        # Calculate the next view date
        calculate_next_view_date = mrs.CalculateEverySecondDayNextViewDate()
        next_view_date = calculate_next_view_date.run(stack_id, odd_even_cd)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        print("Calculated date: {:s}".format(next_view_date_string))

        # Run the test
        update_next_view_date = ms.UpdateNextViewDate()
        update_next_view_date.run(stack_id, next_view_date)

"""
A class to test RetrieveStackById

Jaco Koekemoer
2023-04-07
"""
class RetrieveStackByIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 1

        # Run the test
        retrieve_stack = ms.RetrieveStackById()
        result = retrieve_stack.run(id)

        # Assert result
        ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveAllStacks

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllStacksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stack = ms.RetrieveAllStacks()
        result = retrieve_stack.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveActiveStacksByCategoryId

Jaco Koekemoer
2023-04-07
"""
class RetrieveActiveStacksByCategoryIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        category_id = 1

        # Run the test
        retrieve_stack = ms.RetrieveActiveStacksByCategoryId()
        result = retrieve_stack.run(category_id)

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveScheduledActiveStacks

Jaco Koekemoer
2023-04-12
"""
class RetrieveScheduledActiveStacksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = ms.RetrieveScheduledActiveStacks()
        result = retrieve_stacks.run()
        print(result)

        # Assert results
        ut.TestCase.assertTrue(len(result) > 0, True)

"""
A class to test RetrieveDailyActiveStacks

Jaco Koekemoer
2023-04-12
"""
class RetrieveDailyActiveStacksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = ms.RetrieveDailyActiveStacks()
        result = retrieve_stacks.run()
        print(result)

        # Assert results
        ut.TestCase.assertTrue(len(result) > 0, True)

"""
A class to test RetrieveStacksForReview

Jaco Koekemoer
2023-04-12
"""
class RetrieveStacksForReviewTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = ms.RetrieveStacksForReview()
        result = retrieve_stacks.run()
        print(result)

        # Assert results
        ut.TestCase.assertTrue(len(result) > 0, True)

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddStackTest)
# suite = loader.loadTestsFromTestCase(UpdateStackTest)
# suite = loader.loadTestsFromTestCase(RetrieveStackByIdTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllStacksTest)
# suite = loader.loadTestsFromTestCase(RetrieveActiveStacksByCategoryIdTest)
# suite = loader.loadTestsFromTestCase(UpdateNextViewDateTest)
# suite = loader.loadTestsFromTestCase(RetrieveScheduledActiveStacksTest)
# suite = loader.loadTestsFromTestCase(RetrieveDailyActiveStacksTest)
suite = loader.loadTestsFromTestCase(RetrieveStacksForReviewTest)

runner = ut.TextTestRunner()
runner.run(suite)
