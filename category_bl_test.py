import unittest as ut
import category_bl as catbl

"""
A test class for AddCategory

Jaco Koekemoer
2023-04-21
"""
class AddCategoryTest(ut.TestCase):

    @staticmethod
    def runTest():
        description = "Test 4"
        parent_id = 2
        active = 1

        category = catbl.Category()
        category.set_description(description)
        category.set_parent_id(parent_id)
        category.set_active(active)

        add_category = catbl.AddCategory()
        add_category.run(category)

"""
A test class for UpdateCategory

Jaco Koekemoer
2023-04-21
"""
class UpdateCategoryTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 6
        description = "Test 4 Update"
        parent_id = 2
        active = 1

        category = catbl.Category()
        category.set_id(id)
        category.set_description(description)
        category.set_parent_id(parent_id)
        category.set_active(active)

        update_category = catbl.UpdateCategory()
        update_category.run(category)

"""
A test class for RetrieveCategoryById

Jaco Koekemoer
2023-04-21
"""
class RetrieveCategoryByIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 5

        category = catbl.Category()
        category.set_id(id)

        # Run the test
        retrieve_category = catbl.RetrieveCategoryById()
        category = retrieve_category.run(id)

        # Assert result
        ut.TestCase.assertFalse(category, None)
        print("ID: {:d}".format(category.get_id()))
        print("Description: {:s}".format(category.get_description()))
        print("Parent Id: {:d}".format(category.get_parent_id()))
        print("Active: {}".format(category.get_active()))
        print(type(category))

"""
A test class for RetrieveAllCategories

Jaco Koekemoer
2023-04-21
"""
class RetrieveAllCategoriesTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_category = catbl.RetrieveAllCategories()
        result = retrieve_category.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A test class for RetrieveAllParentCategories

Jaco Koekemoer
2023-04-21
"""
class RetrieveActiveCategoriesDictTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_parent_categories = catbl.RetrieveActiveCategoriesDict()
        result = retrieve_parent_categories.run()
        print(result)
        print(type(result))

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddCategoryTest)
# suite = loader.loadTestsFromTestCase(UpdateCategoryTest)
# suite = loader.loadTestsFromTestCase(RetrieveCategoryByIdTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllCategoriesTest)
suite = loader.loadTestsFromTestCase(RetrieveActiveCategoriesDictTest)

runner = ut.TextTestRunner()
runner.run(suite)
