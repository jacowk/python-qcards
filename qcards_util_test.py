import unittest as ut
import qcards_util as qu

"""
A test class for function convert_dict_value_to_index()

Jaco Koekemoer
2023-04-22
"""
class ConvertDictValueToIndexTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare dictionary
        fruit = dict()
        fruit["apples"] = 3
        fruit["bananas"] = 7
        fruit["oranges"] = 6

        # Prepare variables
        value = 7
        expected_index = 1

        # Run the test
        qcards_util = qu.QCardsUtil()
        result = qcards_util.convert_dict_value_to_index(fruit, value)
        ut.TestCase.assertTrue(result == expected_index, True)

"""
A test class for function convert_index_to_dict_key()

Jaco Koekemoer
2023-04-23
"""
class ConvertIndexToDictKeyTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare dictionary
        fruit = dict()
        fruit["apples"] = 3
        fruit["bananas"] = 7
        fruit["oranges"] = 6

        # Prepare variables
        index = 1
        expected_key = "bananas"

        # Run the test
        qcards_util = qu.QCardsUtil()
        result = qcards_util.convert_index_to_dict_key(fruit, index)
        ut.TestCase.assertTrue(result == expected_key, True)

"""
A test class for function strip_trailing_new_line(value)

Jaco Koekemoer
2023-05-07
"""
class StripTrailingNewLineTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare variables
        value = "test\n\n\n"

        # Run the test
        qcards_util = qu.QCardsUtil()
        result = qcards_util.strip_trailing_new_line(value)
        print(result)

"""
A test class for function escape_single_quotes(value)

Jaco Koekemoer
2023-05-07
"""
class EscapeSingleQuotesTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare variables
        value = "test\'"
        print(value)

        # Run the test
        qcards_util = qu.QCardsUtil()
        result = qcards_util.escape_single_quotes(value)
        print(result)

"""
A test class for function escape_double_quotes(value)

Jaco Koekemoer
2023-05-07
"""
class EscapeDoubleQuotesTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare variables
        value = "test\""
        print(value)

        # Run the test
        qcards_util = qu.QCardsUtil()
        result = qcards_util.escape_double_quotes(value)
        print(result)

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(ConvertDictValueToIndexTest)
# suite = loader.loadTestsFromTestCase(ConvertIndexToDictKeyTest)
# suite = loader.loadTestsFromTestCase(StripTrailingNewLineTest)
suite = loader.loadTestsFromTestCase(EscapeSingleQuotesTest)
# suite = loader.loadTestsFromTestCase(EscapeDoubleQuotesTest)

runner = ut.TextTestRunner()
runner.run(suite)

"""
# Test convert_tinyint_to_string
value = 0
cards_util = QCardsUtil()
result = cards_util.convert_tinyint_to_string(value)
print(result)
"""

"""
# Test convert_tinyint_to_string
value = "No"
cards_util = QCardsUtil()
result = cards_util.convert_string_to_tinyint(value)
print(result)
"""

"""
# Test convert_tinyint_to_boolean
value = 1
cards_util = QCardsUtil()
result = cards_util.convert_tinyint_to_boolean(value)
print(result)
"""

"""
# Test convert_boolean_to_tinyint
value = False
cards_util = QCardsUtil()
result = cards_util.convert_boolean_to_tinyint(value)
print(result)
"""


