import qcards_db as qcards_db
import qcards_util as qu

"""
A class for creating a new stack in the database.

Jaco Koekemoer
2023-04-07
"""
class AddStackDAO:

    def run(self, description, active, source, category_id):
        # Prepare SQL
        sql = "insert into t_stack(description, active, source, category_id, create_date) \
            values('{:s}', {}, '{:s}', {}, now());".format(description, active, source,
                                                           "NULL" if category_id is None else category_id);
        #print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);

"""
A class for updating a stack in the database.

Jaco Koekemoer
2023-04-07
"""
class UpdateStackDAO:

    def run(self, id, description, active, source, category_id):

        # Prepare SQL
        sql = "update t_stack \
            set description = '{:s}', \
            active = {}, \
            source = '{:s}', \
            category_id = {} \
            where id = {:d};".format(description, active, source, "NULL" if category_id is None else category_id, id)
        #print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
A class to update the next_view_date for a stack.

Jaco Koekemoer
2023-04-10
"""
class UpdateNextViewDateDAO:

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
class RetrieveStackByIdDAO:

    def run(self, id):
        # Prepare SQL
        sql = "select s.id, \
                s.description, \
                s.active, \
                s.source, \
                s.category_id, \
                s.next_view_date, \
                rs.id, \
                lrs.description \
                from t_stack s \
                left join t_review_stage rs on rs.stack_id = s.id \
                left join t_lookup_review_stage lrs on rs.review_stage_cd = lrs.id \
                where s.id = {:d};".format(id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql);

"""
A class for retrieving all stacks

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllStacksDAO:

    def run(self):
        # Prepare SQL
        # sql = "select id, description, active, source, category_id, next_view_date from t_stack;"
        sql = "select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, c.description, rs.id, lrs.description \
                from t_stack s \
                left join t_category c on c.id = s.category_id \
                left join t_review_stage rs on rs.stack_id = s.id \
                left join t_lookup_review_stage lrs on rs.review_stage_cd = lrs.id \
                order by s.description asc;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
A class for retrieving a stacks by category id

Jaco Koekemoer
2023-04-07
"""
class RetrieveActiveStacksByCategoryIdDAO:

    def run(self, category_id, active = None):
        # Prepare SQL
        sql = "select s.id, \
                s.description, \
                s.active, \
                s.source, \
                s.category_id, \
                s.next_view_date, \
                c.description, \
                rs.id, \
                lrs.description \
                from t_stack s \
                left join t_category c on c.id = s.category_id \
                left join t_review_stage rs on rs.stack_id = s.id \
                left join t_lookup_review_stage lrs on rs.review_stage_cd = lrs.id \
                where s.category_id = {:d}".format(category_id)
        active_sql = " and s.active = 1"
        order_by_sql = " order by s.description asc;"
        if active == None:
            sql += order_by_sql
        else:
            sql += active_sql + order_by_sql
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
A class for retrieving a stacks which are active and scheduled for view today
and s.next_view_date <= curdate() - Today or in the past
and rs.review_stage_cd != 1 - Not daily review stage

Jaco Koekemoer
2023-04-12
"""
class RetrieveScheduledActiveStacksDAO:

    def run(self):
        # Prepare SQL
        sql = "select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd, c.description, lrs.description \
                from t_stack s, t_review_stage rs, t_category c, t_lookup_review_stage lrs \
                where s.id = rs.stack_id \
                and s.category_id = c.id \
                and rs.review_stage_cd = lrs.id \
                and s.active = 1 \
                and (s.next_view_date <= curdate() or s.next_view_date is null) \
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
class RetrieveDailyActiveStacksDAO:

    def run(self):
        # Prepare SQL
        sql = "select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd, c.description, lrs.description \
                from t_stack s, t_review_stage rs, t_category c, t_lookup_review_stage lrs \
                where s.id = rs.stack_id \
                and s.category_id = c.id \
                and rs.review_stage_cd = lrs.id \
                and s.active = 1 \
                and rs.review_stage_cd = 1;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)
