import unittest as ut
import stack_bl as sbl

"""
A test class for AddStack

Jaco Koekemoer
2023-04-23
"""
class AddStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test Stack"
        active = 1
        source = "Testing different things"
        stack_id = 2

        stack = sbl.Stack()
        stack.set_description(description)
        stack.set_active(active)
        stack.set_source(source)
        stack.set_stack_id(stack_id)

        add_stack = sbl.AddStack()
        add_stack.run(stack)

"""
A test class for UpdateStack

Jaco Koekemoer
2023-04-23
"""
class UpdateStackTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 6
        description = "Test Stack Update"
        active = 1
        source = "Testing different things again"
        category_id = 2

        stack = sbl.Stack()
        stack.set_id(id)
        stack.set_description(description)
        stack.set_category_id(category_id)
        stack.set_active(active)
        stack.set_source(source)

        update_stack = sbl.UpdateStack()
        update_stack.run(stack)

"""
A test class for RetrieveStackById

Jaco Koekemoer
2023-04-24
"""
class RetrieveStackByIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 5

        stack = sbl.Stack()
        stack.set_id(id)

        # Run the test
        retrieve_stack = sbl.RetrieveStackById()
        stack = retrieve_stack.run(id)

        # Assert result
        ut.TestCase.assertFalse(stack, None)
        print("ID: {:d}".format(stack.get_id()))
        print("Description: {:s}".format(stack.get_description()))
        print("Active: {}".format(stack.get_active()))
        print("Source: {}".format(stack.get_source()))
        print("Category Id: {:d}".format(stack.get_category_id()))
        print("Next View Date: {:%Y-%m-%d}".format(stack.get_next_view_date()))
        print(type(stack))

"""
A test class for RetrieveAllStacks

Jaco Koekemoer
2023-04-24
"""
class RetrieveAllStacksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stack = sbl.RetrieveAllStacks()
        result = retrieve_stack.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A test class for RetrieveActiveStacksByCategoryId

Jaco Koekemoer
2023-04-24
"""
class RetrieveActiveStacksByCategoryIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        category_id = 1

        # Run the test
        retrieve_stack = sbl.RetrieveActiveStacksByCategoryId()
        result = retrieve_stack.run(category_id)

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A test class for RetrieveScheduledActiveStacks

Jaco Koekemoer
2023-04-24
"""
class RetrieveScheduledActiveStacksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stack = sbl.RetrieveScheduledActiveStacks()
        result = retrieve_stack.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A test class for RetrieveDailyActiveStacks

Jaco Koekemoer
2023-04-24
"""
class RetrieveDailyActiveStacksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stack = sbl.RetrieveDailyActiveStacks()
        result = retrieve_stack.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A class to test RetrieveStacksForReviewDAO

Jaco Koekemoer
2023-04-12
"""
class RetrieveStacksForReviewTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_stacks = sbl.RetrieveStacksForReview()
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
# suite = loader.loadTestsFromTestCase(RetrieveScheduledActiveStacksTest)
# suite = loader.loadTestsFromTestCase(RetrieveDailyActiveStacksTest)
suite = loader.loadTestsFromTestCase(RetrieveStacksForReviewTest)

runner = ut.TextTestRunner()
runner.run(suite)