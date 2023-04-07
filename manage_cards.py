import qcards_db as qcards_db
import MySQLdb as mysql
import qcards_util as qu
import qcards_date_util as du


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


class AddCard:

    def run(self, summary, front_content, back_content, stack_id, active):
        # Prepare SQL
        sql = "insert into t_card(summary, front_content, back_content, stack_id, view_cnt, group_cnt, active, create_date) \
            values(\"{:s}\", \"{:s}\", \"{:s}\", {:d}, 0, 1, {}, now());".format(summary, front_content, back_content,
                                                                                 stack_id, active)
        print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


class UpdateCard:

    def run(self, id, summary, front_content, back_content, stack_id, view_cnt, group_cnt, active):
        # Prepare SQL
        sql = "update t_card \
            set summary = '{:s}', \
            front_content = '{:s}', \
            back_content = '{:s}', \
            stack_id = {:d}, \
            view_cnt = {:d}, \
            group_cnt = {:d}, \
            active = {}, \
            where id = {:d};".format(summary, front_content, back_content, stack_id, view_cnt, group_cnt, active, id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);


class UpdateViewCnt:

    def run(self, id, new_view_count):
        # Prepare SQL
        sql = "update t_card \
            set view_cnt = {:d}, \
            where id = {:d};".format(new_view_count, id)
        print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


class RetrieveCardById:

    def run(self, card_id):
        # Prepare SQL
        sql = "select id, summary, front_content, back_content, stack_id, view_cnt, group_cnt, active from t_card where id = {:d};".format(
            card_id)
        # print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)


class RetrieveAllCards:

    def run(self):
        # Prepare SQL
        sql = "select summary, front_content, back_content, stack_id, view_cnt, group_cnt, active from t_card;"
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


class RetrieveAllActiveCardsByStackId:

    def run(self, stack_id):
        # Prepare SQL
        sql = "select id, summary, front_content, back_content, stack_id, view_cnt, group_cnt, active \
        from t_card \
        where active = 1 \
        and stack_id = {:d};".format(stack_id)
        # print(sql)

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


class UpdateViewStatistics:

    def run(self, card_id):
        # Retrieve the card
        retrieve_card = RetrieveCardById()
        card = retrieve_card.run(card_id)
        view_count = card[0][5]
        view_count += 1
        last_view_date = du.DateUtil.get_now_as_date_time()

        # Prepare SQL
        sql = "update t_card set view_cnt = {:d}, \
        last_view_date = '{:%Y-%m-%d %H:%M:%S}' \
        where id = {:d};".format(view_count, last_view_date, card_id)
        #print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)


class AdaptRecordsToCards:

    def run(self, records):
        cards = []
        for row in records:
            id = row[0]
            description = row[1]
            active = row[2]
            card = Card(id, description, active)
            cards.append(card);
        return cards


class PrintCards:

    def run(self, cards):
        for card in cards:
            print("{} {} {}".format(card.id, card.description, card.active))
