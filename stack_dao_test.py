import unittest as ut
import stack_dao as sd
import qcards_date_util as qdu
import review_stage_dao as rsd

"""
A class to test AddStackDAO

Jaco Koekemoer
2023-04-07
"""
class AddStackDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test Stack"
        active = 1
        source = "Testing different things"
        category_id = 2

        add_stack = sd.AddStackDAO()
        add_stack.run(description, active, source, category_id)

"""
A class to test UpdateStackDAO

Jaco Koekemoer
2023-04-07
"""
class UpdateStackDAOTest(ut.TestCase):

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

        update_stack = sd.UpdateStackDAO()
        update_stack.run(id, description, active, source, category_id, last_view_date, next_view_date)

"""
A class to test UpdateNextViewDate

Jaco Koekemoer
2023-04-07
"""
class UpdateNextViewDateDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        stack_id = 4
        odd_even_cd = rsd.OddEven.ODD.value

        # Calculate the next view date
        calculate_next_view_date = rsd.CalculateEverySecondDayNextViewDate()
        next_view_date = calculate_next_view_date.run(stack_id, odd_even_cd)
        next_view_date_string = qdu.DateUtil().get_date_as_string(next_view_date)
        print("Calculated date: {:s}".format(next_view_date_string))

        # Run the test
        update_next_view_date = sd.UpdateNextViewDateDAO()
        update_next_view_date.run(stack_id, next_view_date)

"""
A class to test RetrieveStackByIdDAO

Jaco Koekemoer
2023-04-07
"""
class RetrieveStackByIdDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 1

        # Run the test
        retrieve_stack = sd.RetrieveStackByIdDAO()
        result = retrieve_stack.run(id)

        # Assert result
        ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveAllStacksDAO

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllStacksDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stack = sd.RetrieveAllStacksDAO()
        result = retrieve_stack.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveActiveStacksByCategoryIdDAO

Jaco Koekemoer
2023-04-07
"""
class RetrieveActiveStacksByCategoryIdDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        category_id = 1

        # Run the test
        retrieve_stack = sd.RetrieveActiveStacksByCategoryIdDAO()
        result = retrieve_stack.run(category_id)

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveScheduledActiveStacksDAO

Jaco Koekemoer
2023-04-12
"""
class RetrieveScheduledActiveStacksDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = sd.RetrieveScheduledActiveStacksDAO()
        result = retrieve_stacks.run()
        print(result)

        # Assert results
        ut.TestCase.assertTrue(len(result) > 0, True)

"""
A class to test RetrieveDailyActiveStacksDAO

Jaco Koekemoer
2023-04-12
"""
class RetrieveDailyActiveStacksDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = sd.RetrieveDailyActiveStacksDAO()
        result = retrieve_stacks.run()
        print(result)

        # Assert results
        ut.TestCase.assertTrue(len(result) > 0, True)

"""
A class to test RetrieveStacksForReviewDAO

Jaco Koekemoer
2023-04-12
"""
class RetrieveStacksForReviewDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = sd.RetrieveStacksForReviewDAO()
        result = retrieve_stacks.run()
        print(result)

        # Assert results
        ut.TestCase.assertTrue(len(result) > 0, True)

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddStackDAOTest)
# suite = loader.loadTestsFromTestCase(UpdateStackDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveStackByIdDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllStacksDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveActiveStacksByCategoryIdDAOTest)
# suite = loader.loadTestsFromTestCase(UpdateNextViewDateDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveScheduledActiveStacksDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveDailyActiveStacksDAOTest)
suite = loader.loadTestsFromTestCase(RetrieveStacksForReviewDAOTest)

runner = ut.TextTestRunner()
runner.run(suite)
