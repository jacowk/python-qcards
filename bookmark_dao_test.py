import unittest as ut
import bookmark_dao as bd

"""
A unit test for AddBookmark

Jaco Koekemoer
2023-04-17
"""
class AddBookmarkTest(ut.TestCase):

    @staticmethod
    def runTest():
        stack_id = -1
        card_id = 9
        active = 1

        add_bookmark = bd.AddBookmark()
        add_bookmark.run(stack_id, card_id, active)

"""
A unit test for UpdateBookmark

Jaco Koekemoer
2023-04-17
"""
class UpdateBookmarkTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 1
        active = 0

        update_bookmark = bd.UpdateBookmark()
        update_bookmark.run(id, active)

"""
A unit test for RetrieveBookmarkById

Jaco Koekemoer
2023-04-17
"""
class RetrieveBookmarkByIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 1

        # Run the test
        retrieve_bookmark = bd.RetrieveBookmarkById()
        result = retrieve_bookmark.run(id)

        # Assert result
        ut.TestCase.assertTrue(len(result) > 0, True)
        print(result)
        print(type(result))

"""
A unit test for RetrieveAllBookmarksTest

Jaco Koekemoer
2023-04-17
"""
class RetrieveAllBookmarksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_bookmark = bd.RetrieveAllBookmarks()
        result = retrieve_bookmark.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

"""
A unit test for RetrieveAllActiveBookmarksTest

Jaco Koekemoer
2023-04-17
"""
class RetrieveAllActiveBookmarksTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_bookmark = bd.RetrieveAllActiveBookmarks()
        result = retrieve_bookmark.run()

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddBookmarkTest)
# suite = loader.loadTestsFromTestCase(UpdateBookmarkTest)
# suite = loader.loadTestsFromTestCase(RetrieveBookmarkByIdTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllBookmarksTest)
suite = loader.loadTestsFromTestCase(RetrieveAllActiveBookmarksTest)

runner = ut.TextTestRunner()
runner.run(suite)
