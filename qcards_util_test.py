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

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(ConvertDictValueToIndexTest)
suite = loader.loadTestsFromTestCase(ConvertIndexToDictKeyTest)

runner = ut.TextTestRunner()
runner.run(suite)
