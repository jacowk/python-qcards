import unittest as ut
import manage_stacks as ms

class AddStackTest(ut.TestCase):

    def runTest(self):
        description = "Java Lang Package"
        active = 1
        source = "www.oracle.com"
        category_id = 2

        add_stack = ms.AddStack()
        add_stack.run(description, active, source, category_id)

class UpdateStackTest(ut.TestCase):

    def runTest(self):
        id = 1
        description = "Java Lang Package Updated"
        active = 1
        source = "www.oracle.com"
        category_id = 1

        update_stack = ms.UpdateStack()
        update_stack.run(id, description, active, source, category_id)

class RetrieveStackByIdTest(ut.TestCase):

    def runTest(self):
        # Setup parameter
        id = 1

        # Run the test
        retrieve_stack = ms.RetrieveStackById()
        result = retrieve_stack.run(id)

        # Assert result
        self.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

class RetrieveAllStacksTest(ut.TestCase):

    def runTest(self):
        # Run the test
        retrieve_stack = ms.RetrieveAllStacks()
        result = retrieve_stack.run()

        # Assert result
        self.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

class RetrieveStackByCategoryIdTest(ut.TestCase):

    def runTest(self):
        # Setup parameter
        category_id = 2

        # Run the test
        retrieve_stack = ms.RetrieveStackByCategoryId()
        result = retrieve_stack.run(category_id)

        # Assert result
        self.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
#suite = loader.loadTestsFromTestCase(AddStackTest)
#suite = loader.loadTestsFromTestCase(UpdateStackTest)
#suite = loader.loadTestsFromTestCase(RetrieveStackByIdTest)
#suite = loader.loadTestsFromTestCase(RetrieveAllStacksTest)
suite = loader.loadTestsFromTestCase(RetrieveStackByCategoryIdTest)

runner = ut.TextTestRunner()
runner.run(suite)
