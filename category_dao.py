import qcards_db as qcards_db

"""
Add a category

Jaco Koekemoer
2023-04-07
"""
class AddCategoryDAO:

    def run(self, description, parent_id, active):
        # Prepare SQL
        sql = "insert into t_category(description, parent_id, active, create_date, last_modified_date) \
                values('{:s}', {}, {}, current_timestamp(), current_timestamp());".format(
                description, "NULL" if parent_id is None else parent_id, active)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Update a category

Jaco Koekemoer
2023-04-07
"""
class UpdateCategoryDAO:

    def run(self, id, description, parent_id, active):
        # Prepare SQL
        sql = "update t_category set description = '{:s}', \
        parent_id = {}, \
        active = {} \
        where id = {:d};".format(description, "NULL" if parent_id is None else parent_id, active, id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Retrieve a category by id

Jaco Koekemoer
2023-04-07
"""
class RetrieveCategoryByIdDAO:

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
class RetrieveAllCategoriesDAO:

    def run(self):
        # Prepare SQL
        # sql = "select id, description, parent_id, active from t_category;"
        sql = "select c1.id, \
                c1.description, \
                c1.parent_id, \
                c1.active, \
                c2.description as parent_description \
                from t_category c1 \
                left join t_category c2 on c2.id = c1.parent_id \
                order by c1.description asc;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
Retrieve all active categories

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllActiveCategoriesDAO:

    def run(self):
        # Prepare SQL
        sql = "select id, description, parent_id, active from t_category where active = 1;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)
