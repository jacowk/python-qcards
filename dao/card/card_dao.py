import os
import sys
sys.path.insert(0, '/home/jaco/Projects/python-projects/python_qcards')

from util import qcards_util as qu
from util import qcards_date_util as du
from util import qcards_db as qcards_db
from enum import Enum



"""
An enum representing the data in t_lookup_group

Jaco Koekemoer
2023-04-13
"""

class CardGroup(Enum):
    FRONT = 1
    MIDDLE = 2
    BACK = 3


"""
A class for representing a card

Jaco Koekemoer
2023-04-07
"""


class Card:

    def __init__(self, id, summary, front_content, back_content, stack_id, view_cnt, group_cnt, active):
        self.id = id
        self.summary = summary
        self.front_content = front_content
        self.back_content = back_content
        self.stack_id = stack_id
        self.view_cnt = view_cnt
        self.group_cnt = group_cnt
        self.active = active

    def convert_to_list(self):
        return [self.id, self.summary, self.front_content, self.back_content, self.stack_id, self.view_cnt,
                self.group_cnt, self.active]


"""
A class for creating a new card

Jaco Koekemoer
2023-04-07
"""


class AddCard:

    def run(self, summary, front_content, back_content, stack_id, active):
        # Prepare SQL
        sql = "insert into t_card(summary, front_content, back_content, stack_id, view_count, group_cd, active, create_date) \
            values(\"{:s}\", \"{:s}\", \"{:s}\", {:d}, 0, 1, {}, now());".format(summary, front_content, back_content,
                                                                                 stack_id, active)
        print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


"""
A class for updating a card

Jaco Koekemoer
2023-04-07
"""


class UpdateCard:

    def run(self, id, summary, front_content, back_content, stack_id, view_count, group_cnt, active):
        # Prepare SQL
        sql = "update t_card \
            set summary = '{:s}', \
            front_content = '{:s}', \
            back_content = '{:s}', \
            stack_id = {:d}, \
            view_count = {:d}, \
            group_cnt = {:d}, \
            active = {}, \
            where id = {:d};".format(summary, front_content, back_content, stack_id, view_count, group_cnt, active, id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);


"""
A class for updating the view count for a card

Jaco Koekemoer
2023-04-07
"""


class UpdateViewCnt:

    def run(self, id, new_view_count):
        # Prepare SQL
        sql = "update t_card \
            set view_count = {:d}, \
            where id = {:d};".format(new_view_count, id)
        print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


"""
A class for retrieving a card by id

Jaco Koekemoer
2023-04-07
"""


class RetrieveCardById:

    def run(self, card_id):
        # Prepare SQL
        sql = "select id, summary, front_content, back_content, stack_id, view_count, group_cnt, active from t_card where id = {:d};".format(
            card_id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)


"""
A class for retrieving all cards

Jaco Koekemoer
2023-04-07
"""


class RetrieveAllCards:

    def run(self):
        # Prepare SQL
        sql = "select summary, front_content, back_content, stack_id, view_count, group_cnt, active from t_card;"
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        cards = execute_query.execute(sql)
        return cards

    def convert_active(self, cards):
        converted_cards = ()
        qcards_util = qu.QCardsUtil()
        for card in cards:
            converted_card = (card[0], card[1], qcards_util.convert_tinyint_to_boolean(card[2]))
            converted_cards = converted_cards + (converted_card,)  # Building up a tuple of tuples
        return converted_cards


"""
A class for retrieving all active cards by stack id

Jaco Koekemoer
2023-04-07
"""


class RetrieveAllActiveCardsByStackId:

    def run(self, stack_id, order_group=False):
        # Prepare SQL
        sql = "select id, summary, front_content, back_content, stack_id, view_count, group_cd, active \
        from t_card \
        where active = 1 \
        and stack_id = {:d}".format(stack_id)
        if order_group == True:
            sql += " order by group_cd asc, id asc;"
        else:
            sql += " order by id asc;"
        print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        # cards = execute_query.execute(sql)
        # return self.convert_active(cards)
        return execute_query.execute(sql)

    def convert_active(self, cards):
        converted_cards = ()
        qcards_util = qu.QCardsUtil()
        for card in cards:
            converted_card = (card[0], card[1], qcards_util.convert_tinyint_to_boolean(card[2]))
            converted_cards = converted_cards + (converted_card,)  # Building up a tuple of tuples
        return converted_cards


"""
A class for updating the view staticstics for a card, meaning the view count is incremented by 1, and the last_view_date is updated to today

Jaco Koekemoer
2023-04-07
"""


class UpdateViewStatistics:

    def run(self, card_id):
        # Retrieve the card
        retrieve_card = RetrieveCardById()
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


class UpdateCardGroup:

    def run(self, card_id, group_cd):
        # Prepare SQL
        sql = "update t_card set group_cd = {:d} \
                where id = {:d};".format(group_cd, card_id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)
