import unittest as ut
import category_dao as catd


class AddCategoryDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test 3"
        parent_id = 2
        active = 1

        add_category = catd.AddCategoryDAO()
        add_category.run(description, parent_id, active)


class AddMultipleCategoriesTest(ut.TestCase):

    @staticmethod
    def runTest():
        categories = ['Java', 'Python', 'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'JQuery']
        for category in categories:
            add_category = catd.AddCategoryDAO()
            parent_id = None
            active = True
            add_category.run(category, parent_id, active)


class UpdateCategoryDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 5
        description = "Sub Test 3"
        parent_id = 2
        active = 1

        update_category = catd.UpdateCategoryDAO()
        update_category.run(id, description, parent_id, active)


class RetrieveCategoryByIdDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 5

        # Run the test
        retrieve_category = catd.RetrieveCategoryByIdDAO()
        result = retrieve_category.run(id)

        # Assert result
        ut.TestCase.assertTrue(len(result) > 0, True)
        print(result)
        print(type(result))


class RetrieveAllCategoriesDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_category = catd.RetrieveAllCategoriesDAO()
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
# suite = loader.loadTestsFromTestCase(AddCategoryDAOTest)
# suite = loader.loadTestsFromTestCase(UpdateCategoryDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveCategoryByIdDAOTest)
suite = loader.loadTestsFromTestCase(RetrieveAllCategoriesDAOTest)

runner = ut.TextTestRunner()
runner.run(suite)
