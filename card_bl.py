import card_dao as cd
import qcards_util as qu
import csv

"""
A card domain class

Jaco Koekemoer
2023-04-27
"""
class Card:

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_front_content(self):
        return self.front_content

    def set_front_content(self, front_content):
        self.front_content = front_content

    def get_back_content(self):
        return self.back_content

    def set_back_content(self, back_content):
        self.back_content = back_content

    def get_stack_id(self):
        return self.stack_id

    def set_stack_id(self, stack_id):
        self.stack_id = stack_id

    def get_view_count(self):
        return self.view_count

    def set_view_count(self, view_count):
        self.view_count = view_count

    def get_group_cd(self):
        return self.group_cd

    def set_group_cd(self, group_cd):
        self.group_cd = group_cd

    def get_active(self):
        return self.active

    def set_active(self, active):
        self.active = active

    def get_last_view_date(self):
        return self.last_view_date

    def set_last_view_date(self, last_view_date):
        self.last_view_date = last_view_date

    def get_stack_description(self):
        return self.stack_description

    def set_stack_description(self, stack_description):
        self.stack_description = stack_description

    def get_category_description(self):
        return self.category_description

    def set_category_description(self, category_description):
        self.category_description = category_description

    def get_category_id(self):
        return self.category_id

    def set_category_id(self, category_id):
        self.category_id = category_id

"""
Business layer for adding cards

Jaco Koekemoer
2023-04-27
"""
class AddCard:

    def run(self, card):
        # Massage the data
        util = qu.QCardsUtil()
        card.set_front_content(util.strip_trailing_new_line(card.get_front_content()))
        card.set_front_content(util.escape_single_quotes(card.get_front_content()))
        card.set_front_content(util.escape_double_quotes(card.get_front_content()))
        card.set_front_content(util.escape_semi_colon(card.get_front_content()))

        card.set_back_content(util.strip_trailing_new_line(card.get_back_content()))
        card.set_back_content(util.escape_single_quotes(card.get_back_content()))
        card.set_back_content(util.escape_double_quotes(card.get_back_content()))
        card.set_back_content(util.escape_semi_colon(card.get_back_content()))

        # Call DAO
        add_card_dao = cd.AddCardDAO()
        # title, front_content, back_content, stack_id, active
        add_card_dao.run(card.title, card.front_content, card.back_content, card.stack_id, card.active)

"""
Business layer for updating cards

Jaco Koekemoer
2023-04-27
"""
class UpdateCard:

    def run(self, card):
        # Massage the data
        util = qu.QCardsUtil()
        card.set_front_content(util.strip_trailing_new_line(card.get_front_content()))
        card.set_front_content(util.escape_single_quotes(card.get_front_content()))
        card.set_front_content(util.escape_double_quotes(card.get_front_content()))
        card.set_front_content(util.escape_semi_colon(card.get_front_content()))

        card.set_back_content(util.strip_trailing_new_line(card.get_back_content()))
        card.set_back_content(util.escape_single_quotes(card.get_back_content()))
        card.set_back_content(util.escape_double_quotes(card.get_back_content()))
        card.set_back_content(util.escape_semi_colon(card.get_back_content()))

        # Call DAO
        update_card_dao = cd.UpdateCardDAO()
        update_card_dao.run(card.id, card.title, card.front_content, card.back_content, card.stack_id, card.active)

"""
Business layer for updating the view count for a card

Jaco Koekemoer
2023-04-27
"""
class UpdateViewCnt:

    def run(self, card):
        update_view_count = cd.UpdateViewCntDAO()
        update_view_count.run(card.id, card.view_count)

"""
Business layer for retrieve a card by id

Jaco Koekemoer
2023-04-27
"""
class RetrieveCardById:

    def run(self, id):
        retrieve_card_dao = cd.RetrieveCardByIdDAO()
        result = retrieve_card_dao.run(id) # Returns 2 dimensional tuple
        # id, title, front_content, back_content, stack_id, view_count, group_cd, active, last_view_date

        # Convert result to Category class
        card = Card()
        card.set_id(result[0][0])
        card.set_title(result[0][1])
        card.set_front_content(result[0][2])
        card.set_back_content(result[0][3])
        card.set_stack_id(result[0][4])
        card.set_view_count(result[0][5])
        card.set_group_cd(result[0][6])
        qcards_util = qu.QCardsUtil()
        card.set_active(qcards_util.convert_tinyint_to_boolean(result[0][7]))
        card.set_last_view_date(result[0][8])
        card.set_stack_description(result[0][9])
        card.set_category_description(result[0][10])
        card.set_category_id(result[0][11])
        return card


"""
Business layer for retrieve all cards

Jaco Koekemoer
2023-04-27
"""
class RetrieveAllCards:

    def run(self):
        retrieve_all_cards = cd.RetrieveAllCardsDAO()
        cards = retrieve_all_cards.run()  # Returns 2 dimensional tuple
        # id, title, front_content, back_content, stack_id, view_count, group_cd, active, last_view_date

        # Convert data for front-end display
        converted_cards = ()
        qcards_util = qu.QCardsUtil()
        for card in cards:
            converted_card = (
                card[0],  # id
                card[1],  # title
                card[2],  # front_content
                card[3],  # back_content
                card[4],  # stack_id
                card[5],  # view_count
                card[6],  # group_cd
                qcards_util.convert_tinyint_to_boolean(card[7]),  # active
                card[8] if card[8] is not None else '',  # last_view_date
                card[9],  # stack_description
                card[10],  # category_description
            )
            converted_cards = converted_cards + (converted_card,)  # Building up a tuple of tuples
        return converted_cards

"""
Business layer for retrieve all cards by stack id

Jaco Koekemoer
2023-04-27
"""
class RetrieveActiveCardsByStackId:

    def run(self, stack_id, active = None, order_group = False):
        retrieve_all_cards = cd.RetrieveActiveCardsByStackIdDAO()
        cards = retrieve_all_cards.run(stack_id, active, order_group)  # Returns 2 dimensional tuple
        # id, title, front_content, back_content, stack_id, view_count, group_cd, active, last_view_date

        # Convert data for front-end display
        converted_cards = ()
        qcards_util = qu.QCardsUtil()
        for card in cards:
            converted_card = (
                card[0],  # id
                card[1],  # title
                card[2],  # front_content
                card[3],  # back_content
                card[4],  # stack_id
                card[5],  # view_count
                card[6],  # group_cd
                qcards_util.convert_tinyint_to_boolean(card[7]),  # active
                card[8] if card[8] is not None else '', # last_view_date
                card[9],  # stack_description
                card[10],  # category_description
            )
            converted_cards = converted_cards + (converted_card,)  # Building up a tuple of tuples
        return converted_cards

"""
Business layer for updating view statistics

Jaco Koekemoer
2023-04-27
"""
class UpdateViewStatistics:

    def run(self, card_id):
        update_view_statictics = cd.UpdateViewStatisticsDAO()
        update_view_statictics.run(card_id)

"""
Business layer for updating the card group

Jaco Koekemoer
2023-04-27
"""
class UpdateCardGroup:

    def run(self, card_id, group_cd):
        update_card_group = cd.UpdateCardGroupDAO()
        update_card_group.run(card_id, group_cd)

"""
Business layer for importing cards from file

Jaco Koekemoer
2023-05-06
"""
class ImportCards:

    def run(self, stack_id, filename):
        with open(filename, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter='|')
            cnt = 1

            for row in datareader:
                if cnt == 1:
                    cnt += 1
                    continue  # Skip first line with only column names

                title = row[0]
                front_content = row[1]
                back_content = row[2]
                active = 1

                #print(title, front_content, back_content, stack_id, active)

                #add_card = cd.AddCardDAO()
                #add_card.run(title, front_content, back_content, stack_id, active)

                card = Card()
                card.set_title(title)
                card.set_front_content(front_content)
                card.set_back_content(back_content)
                card.set_stack_id(stack_id)
                card.set_active(active)

                add_card = AddCard()
                add_card.run(card)



