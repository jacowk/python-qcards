import unittest as ut
import category_dao as catd


class AddCategoryTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test 2"
        active = 1

        add_category = catd.AddCategory()
        add_category.run(description, active)


class AddMultipleCategoriesTest(ut.TestCase):

    @staticmethod
    def runTest():
        categories = ['Java', 'Python', 'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'JQuery']
        for category in categories:
            add_category = catd.AddCategory()
            add_category.run(category, True)


class UpdateCategoryTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 1
        description = "Java"
        active = 1

        update_category = catd.UpdateCategory()
        update_category.run(id, description, active)


class RetrieveCategoryByIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 1

        # Run the test
        retrieve_category = catd.RetrieveCategoryById()
        result = retrieve_category.run(id)

        # Assert result
        ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))


class RetrieveAllCategoriesTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_category = catd.RetrieveAllCategories()
        result = retrieve_category.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))


# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddMultipleCategoriesTest)
suite = loader.loadTestsFromTestCase(AddCategoryTest)
# suite = loader.loadTestsFromTestCase(UpdateCategoryTest)
# suite = loader.loadTestsFromTestCase(RetrieveCategoryByIdTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllCategoriesTest)

runner = ut.TextTestRunner()
runner.run(suite)