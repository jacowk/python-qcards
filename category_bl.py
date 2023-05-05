import category_dao as catd
import qcards_util as qu
import category_constant as catc

"""
A category domain class

Jaco Koekemoer
2023-04-07
"""
class Category:

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_parent_id(self):
        return self.parent_id

    def set_parent_id(self, parent_id):
        self.parent_id = parent_id

    def get_active(self):
        return self.active

    def set_active(self, active):
        self.active = active

"""
Business layer for adding categories

Jaco Koekemoer
2023-04-17
"""
class AddCategory:

    def run(self, category):
        add_category_dao = catd.AddCategoryDAO()
        add_category_dao.run(category.description, category.parent_id, category.active)

"""
Business layer for updating categories

Jaco Koekemoer
2023-04-21
"""
class UpdateCategory:

    def run(self, category):
        update_category_dao = catd.UpdateCategoryDAO()
        update_category_dao.run(category.id, category.description, category.parent_id, category.active)

"""
Business layer for retrieve a category by id

Jaco Koekemoer
2023-04-21
"""
class RetrieveCategoryById:

    def run(self, id):
        retrieve_category_dao = catd.RetrieveCategoryByIdDAO()
        result = retrieve_category_dao.run(id) # Returns 2 dimensional tuple
        # id, description, parent_id, active

        # Convert result to Category class
        category = Category()
        category.set_id(result[0][0])
        category.set_description(result[0][1])
        category.set_parent_id(result[0][2])
        qcards_util = qu.QCardsUtil()
        category.set_active(qcards_util.convert_tinyint_to_boolean(result[0][3]))
        return category

"""
Business layer for retrieving all categories

Jaco Koekemoer
2023-04-21
"""
class RetrieveAllCategories:

    def run(self):
        # Retrieve all categories via the DAO
        retrieve_category = catd.RetrieveAllCategoriesDAO()
        categories = retrieve_category.run()

        # Convert data for front-end display
        converted_categories = ()
        qcards_util = qu.QCardsUtil()
        for category in categories:
            converted_category = (
                category[0], # id
                category[1], # description
                category[4] if category[4] != None else '', # parent_description
                qcards_util.convert_tinyint_to_boolean(category[3]), # active
            )
            converted_categories = converted_categories + (converted_category,)  # Building up a tuple of tuples
        return converted_categories

"""
Business layer for retrieving all categories as a dictionary

Jaco Koekemoer
2023-04-21
"""
class RetrieveAllCategoriesDict:

    def run(self):
        # Retrieve all categories via the DAO
        retrieve_category = catd.RetrieveAllCategoriesDAO()
        categories = retrieve_category.run()

        # Convert data for front-end display
        parent_dictionary = dict()
        parent_dictionary[catc.CategoryConstants.SELECT_CATEGORY.value] = -1
        for category in categories:
            parent_dictionary[category[1]] = category[0] # description: id
        return parent_dictionary
