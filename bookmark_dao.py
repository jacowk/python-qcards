import traceback
import qcards_db as qcards_db

class Bookmark:

    def __init__(self, id, stack_id, card_id, active):
        self.id = id
        self.stack_id = stack_id
        self.card_id = card_id
        self.active = active

"""
Add a bookmark

Jaco Koekemoer
2023-04-17
"""
class AddBookmark:

    def run(self, stack_id, card_id, active):
        try:
            # Prepare SQL
            sql = "insert into t_bookmark(stack_id, card_id, active, create_date) \
                values({:d}, {:d}, {}, NOW());".format(stack_id, card_id, active)
            # print(sql)

            # Run the query
            execute_query = qcards_db.QCardsExecuteQuery()
            execute_query.execute(sql)
        except Exception as e:
            traceback.print_exc()
            raise

"""
Update a bookmark

Jaco Koekemoer
2023-04-17
"""
class UpdateBookmark:

    def run(self, id, active):
        try:
            # Prepare SQL
            sql = "update t_bookmark \
                    set active = {}, \
                        last_modified_date = NOW() \
                    where id = {:d};".format(active, id)
            # print(sql)

            # Run the query
            execute_query = qcards_db.QCardsExecuteQuery()
            execute_query.execute(sql)
        except Exception as e:
            traceback.print_exc()
            raise

"""
Retrieve a bookmark by id

Jaco Koekemoer
2023-04-17
"""
class RetrieveBookmarkById:

    def run(self, id):
        try:
            # Prepare SQL
            sql = "select id, stack_id, card_id, active from t_bookmark where id = {:d};".format(id)
            # print(sql)

            # Run the query
            execute_query = qcards_db.QCardsExecuteSelectQuery()
            return execute_query.execute(sql)
        except Exception as e:
            traceback.print_exc()
            raise

"""
Retrieve all bookmarks

Jaco Koekemoer
2023-04-17
"""
class RetrieveAllBookmarks:

    def run(self):
        try:
            # Prepare SQL
            sql = "select id, stack_id, card_id, active from t_bookmark;"
            # print(sql)

            # Run the query
            execute_query = qcards_db.QCardsExecuteSelectQuery()
            return execute_query.execute(sql)
        except Exception as e:
            traceback.print_exc()
            raise

"""
Retrieve all active bookmarks

Jaco Koekemoer
2023-04-17
"""
class RetrieveAllActiveBookmarks:

    def run(self):
        try:
            # Prepare SQL
            sql = "select id, stack_id, card_id, active from t_bookmark where active = 1;"
            # print(sql)

            # Run the query
            execute_query = qcards_db.QCardsExecuteSelectQuery()
            return execute_query.execute(sql)
        except Exception as e:
            traceback.print_exc()
            raise
