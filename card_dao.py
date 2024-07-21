import qcards_db as qcards_db
import qcards_date_util as du

"""
A class for creating a new card

Jaco Koekemoer
2023-04-07
"""
class AddCardDAO:

    def run(self, title, front_content, back_content, stack_id, active):
        # Prepare SQL
        sql = "insert into t_card(title, front_content, back_content, stack_id, view_count, group_cd, active, create_date) \
            values(\"{:s}\", \"{:s}\", \"{:s}\", {:d}, 0, 1, {}, now());".format(title, front_content, back_content,
                                                                                 stack_id, active)
        #print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


"""
A class for updating a card

Jaco Koekemoer
2023-04-07
"""
class UpdateCardDAO:

    def run(self, id, title, front_content, back_content, stack_id, active):
        # Prepare SQL
        sql = "update t_card \
            set title = '{:s}', \
            front_content = '{:s}', \
            back_content = '{:s}', \
            stack_id = {:d}, \
            active = {} \
            where id = {:d};".format(title, front_content, back_content, stack_id, active, id)
        #print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);


"""
A class for updating the view count for a card

Jaco Koekemoer
2023-04-07
"""
class UpdateViewCntDAO:

    def run(self, id, new_view_count):
        # Prepare SQL
        sql = "update t_card \
            set view_count = {:d} \
            where id = {:d};".format(new_view_count, id)
        #print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
A class for retrieving a card by id

Jaco Koekemoer
2023-04-07
"""
class RetrieveCardByIdDAO:

    def run(self, id):
        # Prepare SQL
        sql = "select c.id, \
                c.title, \
                c.front_content, \
                c.back_content, \
                c.stack_id, \
                c.view_count, \
                c.group_cd, \
                c.active, \
                c.last_view_date, \
                s.description, \
                cat.description, \
                cat.id \
                from t_card c \
                left join t_stack s on c.stack_id = s.id \
                left join t_category cat on s.category_id = cat.id \
                where c.id = {:d};".format(id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
A class for retrieving all cards

Jaco Koekemoer
2023-04-07
"""
class RetrieveAllCardsDAO:

    def run(self):
        # Prepare SQL
        sql = "select c.id, \
                c.title, \
                c.front_content, \
                c.back_content, \
                c.stack_id, \
                c.view_count, \
                c.group_cd, \
                c.active, \
                c.last_view_date, \
                s.description, \
                cat.description \
                from t_card c \
                left join t_stack s on c.stack_id = s.id \
                left join t_category cat on s.category_id = cat.id;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)

"""
A class for retrieving all active cards by stack id

Jaco Koekemoer
2023-04-07
"""
class RetrieveActiveCardsByStackIdDAO:

    def run(self, stack_id, active = None, order_group = False):
        # Prepare SQL
        sql = "select c.id, \
                c.title, \
                c.front_content, \
                c.back_content, \
                c.stack_id, \
                c.view_count, \
                c.group_cd, \
                c.active, \
                c.last_view_date, \
                s.description, \
                cat.description \
                from t_card c \
                left join t_stack s on c.stack_id = s.id \
                left join t_category cat on s.category_id = cat.id \
                where c.stack_id = {:d}".format(stack_id)

        # Add the active clause, to be used mostly for reviewing the cards
        if active:
            sql += " and c.active = 1"

        # Add the group clause, to be used mostly for reviewing the cards
        if order_group:
            sql += " order by group_cd asc, id asc;"
        else:
            sql += " order by id asc;"
        #print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)


"""
A class for updating the view staticstics for a card, meaning the view count is incremented by 1, and the last_view_date is updated to today

Jaco Koekemoer
2023-04-07
"""
class UpdateViewStatisticsDAO:

    def run(self, card_id):
        # Retrieve the card
        retrieve_card = RetrieveCardByIdDAO()
        card = retrieve_card.run(card_id)
        view_count = card[0][5]
        view_count += 1
        last_view_date = du.DateUtil.get_now_as_date_time()

        # Prepare SQL
        sql = "update t_card set view_count = {:d}, \
        last_view_date = '{:%Y-%m-%d %H:%M:%S}' \
        where id = {:d};".format(view_count, last_view_date, card_id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


"""
A class for updating card group in t_card. The enum CardGroup defines the groups that can be defined.

Jaco Koekemoer
2023-04-07
"""
class UpdateCardGroupDAO:

    def run(self, card_id, group_cd):
        # Prepare SQL
        sql = "update t_card set group_cd = {:d} \
                where id = {:d};".format(group_cd, card_id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)
