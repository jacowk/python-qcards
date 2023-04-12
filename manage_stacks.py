import qcards_db as qcards_db
import MySQLdb as mysql
import qcards_util as qu

"""
A class representing a Stack.

Jaco Koekemoer
2023-04-07
"""
class Stack:

    def __init__(self, id, description, active, source, category_id, last_view_date, next_view_date):
        self.id = id
        self.description = description
        self.active = active
        self.source = source
        self.category_id = category_id
        self.last_view_date = last_view_date
        self.next_view_date = next_view_date

    def convert_to_list(self):
        return [self.id, self.description, self.active, self.source, self.category_id, self.last_view_date,
                self.next_view_date]

"""
A class for creating a new stack in the database.

Jaco Koekemoer
2023-04-07
"""
class AddStack:

    def run(self, description, active, source, category_id):
        # Prepare SQL
        sql = "insert into t_stack(description, active, source, category_id, create_date) \
            values('{:s}', {}, '{:s}', {:d}, now());".format(description, active, source, category_id);
        #print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);

"""
A class for updating a stack in the database.

Jaco Koekemoer
2023-04-07
"""
class UpdateStack:

    def run(self, id, description, active, source, category_id):

        # Prepare SQL
        sql = "update t_stack \
            set description = '{:s}', \
            active = {}, \
            source = '{:s}', \
            category_id = {:d}, \
            where id = {:d};".format(description, active, source, category_id, id)
        #print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
A class to update the next_view_date for a stack.

Jaco Koekemoer
2023-04-10
"""
class UpdateNextViewDate:

    def run(self, stack_id, next_view_date):
        # Prepare SQL
        sql = "update t_stack set next_view_date = '{:%Y-%m-%d}' where id = {:d};".format(next_view_date, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
A class for retrieving a stack by id

Jaco Koekemoer
2023-04-07
"""
class RetrieveStackById:

    def run(self, id):
        # Prepare SQL
        sql = "select id, description, active, source, category_id, next_view_date from t_stack where id = {:d};".format(
            id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql);

"""
A class for retrieving all stacks

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllStacks:

    def run(self):
        # Prepare SQL
        sql = "select id, description, active, source, category_id, next_view_date from t_stack;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        # stacks = execute_query.execute(sql);
        # return self.convert_active(stacks)
        return execute_query.execute(sql)

    def convert_active(self, stacks):
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            converted_stack = (stack[0], stack[1], qcards_util.convert_tinyint_to_boolean(stack[2]), stack[3], stack[4])
            converted_stacks = converted_stacks + (converted_stack,)  # Building up a tuple of tuples
        return converted_stacks


"""
A class for retrieving a stacks by category id

Jaco Koekemoer
2023-04-07
"""
class RetrieveActiveStacksByCategoryId:

    def run(self, category_id):
        # Prepare SQL
        sql = "select id, description, active, source, category_id, next_view_date \
        from t_stack \
        where category_id = {:d}\
        and active = 1;".format(
            category_id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        # stacks = execute_query.execute(sql);
        # return self.convert_active(stacks)
        return execute_query.execute(sql)

    def convert_active(self, stacks):
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            converted_stack = (stack[0], stack[1], qcards_util.convert_tinyint_to_boolean(stack[2]), stack[3], stack[4])
            converted_stacks = converted_stacks + (converted_stack,)  # Building up a tuple of tuples
        return converted_stacks

"""
A class for retrieving a stacks which are active and scheduled for view today
and s.next_view_date <= curdate() - Today or in the past
and rs.review_stage_cd != 1 - Not daily review stage

Jaco Koekemoer
2023-04-12
"""
class RetrieveScheduledActiveStacks:

    def run(self):
        # Prepare SQL
        sql = "select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd \
            from t_stack s, t_review_stage rs \
            where s.id = rs.stack_id \
            and s.active = 1 \
            and s.next_view_date <= curdate() \
            and rs.review_stage_cd != 1;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
A class for retrieving a stacks which are active and in the daily review stage.
and rs.review_stage_cd = 1; - Daily

Daily will not have a next_review_date set

Jaco Koekemoer
2023-04-12
"""
class RetrieveDailyActiveStacks:

    def run(self):
        # Prepare SQL
        sql = "select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd \
            from t_stack s, t_review_stage rs \
            where s.id = rs.stack_id \
            and s.active = 1 \
            and rs.review_stage_cd = 1;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
A class for retrieving a stacks to be reviewed

Jaco Koekemoer
2023-04-12
"""
class RetrieveStacksForReview:

    def run(self):
        # Retrieve scheduled stacks
        retrieve_scheduled_stacks = RetrieveScheduledActiveStacks()
        scheduled_stacks = retrieve_scheduled_stacks.run()

        # Retrieve active stacks
        retrieve_daily_stacks = RetrieveDailyActiveStacks()
        daily_stacks = retrieve_daily_stacks.run()

        # Combine stacks and return
        return scheduled_stacks + daily_stacks