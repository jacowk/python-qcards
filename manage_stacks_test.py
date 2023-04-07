import unittest as ut
import manage_stacks as ms
import qcards_date_util as du


class AddStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Behavioral Design Patterns"
        active = 1
        source = "Gang of four book"
        category_id = 1

        add_stack = ms.AddStack()
        add_stack.run(description, active, source, category_id)


class UpdateStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 1
        description = "Java Lang Package"
        active = 1
        source = "www.oracle.com"
        category_id = 1
        last_view_date = du.DateUtil.get_now_as_date_time()
        today = du.DateUtil.get_now_as_date()
        next_view_date = du.DateUtil.add_days(today, 2)

        update_stack = ms.UpdateStack()
        update_stack.run(id, description, active, source, category_id, last_view_date, next_view_date)


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


# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
suite = loader.loadTestsFromTestCase(AddStackTest)
# suite = loader.loadTestsFromTestCase(UpdateStackTest)
# suite = loader.loadTestsFromTestCase(RetrieveStackByIdTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllStacksTest)
#suite = loader.loadTestsFromTestCase(RetrieveActiveStacksByCategoryIdTest)

runner = ut.TextTestRunner()
runner.run(suite)
