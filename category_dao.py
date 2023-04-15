import qcards_db as qcards_db
import MySQLdb as mysql
import qcards_util as qu


class Category:

    def __init__(self, id, description, active):
        self.id = id
        self.description = description
        self.active = active

    def convert_to_list(self):
        return [self.id, self.description, self.active]


class AddCategory:

    def run(self, description, active):
        # Prepare SQL
        sql = "insert into t_category(description, active, create_date, last_modified_date) values('{:s}', {}, current_timestamp(), current_timestamp());".format(
            description, active)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


class UpdateCategory:

    def run(self, id, description, active):
        # Prepare SQL
        sql = "update t_category set description = '{:s}', active = {} where id = {:d};".format(description, active, id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


class RetrieveCategoryById:

    def run(self, id):
        # Prepare SQL
        sql = "select id, description, active from t_category where id = {:d};".format(id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)


class RetrieveAllCategories:

    def run(self):
        # Prepare SQL
        sql = "select id, description, active from t_category;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        categories = execute_query.execute(sql)
        return self.convert_active(categories)


def convert_active(categories):
    converted_categories = ()
    qcards_util = qu.QCardsUtil()
    for category in categories:
        converted_category = (category[0], category[1], qcards_util.convert_tinyint_to_boolean(category[2]))
        converted_categories = converted_categories + (converted_category,)  # Building up a tuple of tuples
    return converted_categories


class RetrieveAllActiveCategories:

    def run(self):
        # Prepare SQL
        sql = "select id, description, active from t_category where active = 1;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        categories = execute_query.execute(sql)
        return convert_active(categories)
