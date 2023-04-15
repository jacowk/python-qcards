import qcards_db as qcards_db
import qcards_util as qu

class Category:

    def __init__(self, id, description, parent_id, active):
        self.id = id
        self.description = description
        self.parent_id = parent_id
        self.active = active

    def convert_to_list(self):
        return [self.id, self.description, self.parent_id, self.active]

"""
Add a category

Jaco Koekemoer
2023-04-07
"""
class AddCategory:

    def run(self, description, parent_id, active):
        # Prepare SQL
        sql = "insert into t_category(description, parent_id, active, create_date, last_modified_date) values('{:s}', {:d}, {}, current_timestamp(), current_timestamp());".format(
            description, parent_id, active)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


"""
Update a category

Jaco Koekemoer
2023-04-07
"""
class UpdateCategory:

    def run(self, id, description, parent_id, active):
        # Prepare SQL
        sql = "update t_category set description = '{:s}', \
        parent_id = {:d}, \
        active = {} \
        where id = {:d};".format(description, parent_id, active, id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


"""
Retrieve a category by id

Jaco Koekemoer
2023-04-07
"""
class RetrieveCategoryById:

    def run(self, id):
        # Prepare SQL
        sql = "select id, description, parent_id, active from t_category where id = {:d};".format(id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)


"""
Retrieve all categories

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllCategories:

    def run(self):
        # Prepare SQL
        sql = "select id, description, parent_id, active from t_category;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        categories = execute_query.execute(sql)
        return convert_active(categories)


def convert_active(categories):
    converted_categories = ()
    qcards_util = qu.QCardsUtil()
    for category in categories:
        converted_category = (category[0], category[1], category[2], qcards_util.convert_tinyint_to_boolean(category[3]))
        converted_categories = converted_categories + (converted_category,)  # Building up a tuple of tuples
    return converted_categories


"""
Retrieve all active categories

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllActiveCategories:

    def run(self):
        # Prepare SQL
        sql = "select id, description, parent_id, active from t_category where active = 1;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        categories = execute_query.execute(sql)
        return convert_active(categories)
