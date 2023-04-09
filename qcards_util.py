import qcards_date_util as qdu

class QCardsUtil:

    # Convert tinyint to String
    def convert_tinyint_to_string(self, value):
        return "Yes" if value == 1 else "No"

    # Convert String to tinyint
    def convert_string_to_tinyint(self, value):
        return 1 if value == "Yes" else 0

    # Convert tinyint to boolean
    def convert_tinyint_to_boolean(self, value):
        return True if value == 1 else False

    # Convert boolean to tinyint
    def convert_boolean_to_tinyint(self, value):
        return 1 if value == True else 0

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
