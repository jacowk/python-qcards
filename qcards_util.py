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
    Given an dictionary, convert a value to an index. For example, I have the following dictionary:
    If I have a dictionary in python. "apples":5, "bananas":7, "oranges":3. Apples is index 0, 
    bananas is index 1 and oranges is index 2. Given 7, I want to get back index 1.
    """
    def convert_dict_value_to_index(self, dictionary, value):
        value_list = list(dictionary.values())
        return value_list.index(value)

    """
    Given an dictionary, convert a given index to the value. For example, I have the following dictionary:
    If I have a dictionary in python. "apples":5, "bananas":7, "oranges":3. Apples is index 0, 
    bananas is index 1 and oranges is index 2. Given 2, I want to get back "bananas".
    """
    def convert_index_to_dict_key(self, dictionary, index):
        value_list = list(dictionary.keys())
        return value_list[index]

    """
    If the selected combobox value is -1, then return None, else return the value. This determines what to 
    store in the database.
    """
    def get_selected_combobox_value(self, value):
        if value == -1:
            return None
        return value

    """
    For a dictionary, return the key where the value matches.
    For example for a dictionary where "Test Stack":3, then if the value is 3, return the key
    """
    def get_dictionary_key_from_value(self, dictionary, value):
        if value is None:
            return None
        for key in dictionary.keys():
            if dictionary[key] == value:
                return key
        return None