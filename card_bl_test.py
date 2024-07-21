import unittest as ut
import card_bl as cbl
import card_constant as cc

"""
A test class for AddCard

Jaco Koekemoer
2023-04-27
"""
class AddCardTest(ut.TestCase):

    @staticmethod
    def runTest():
        title = "Test title 1"
        front_content = "Test front content 1"
        back_content = "Test back content 1"
        stack_id = 1
        active = 1

        card = cbl.Card()
        card.set_title(title)
        card.set_front_content(front_content)
        card.set_back_content(back_content)
        card.set_stack_id(stack_id)
        card.set_active(active)

        add_card = cbl.AddCard()
        add_card.run(card)

"""
A test class for UpdateCard

Jaco Koekemoer
2023-04-27
"""
class UpdateCardTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 26
        title = "Test title 1 update"
        front_content = "Test front content 1 update"
        back_content = "Test back content 1 update"
        stack_id = 2
        active = 1

        card = cbl.Card()
        card.set_id(id)
        card.set_title(title)
        card.set_front_content(front_content)
        card.set_back_content(back_content)
        card.set_stack_id(stack_id)
        card.set_active(active)

        update_card = cbl.UpdateCard()
        update_card.run(card)

"""
A test class for UpdateViewCnt

Jaco Koekemoer
2023-04-27
"""
class UpdateViewCntTest(ut.TestCase):

    @staticmethod
    def runTest():
        id = 26
        new_view_count = 1

        card = cbl.Card()
        card.set_id(id)
        card.set_view_count(new_view_count)

        update_view_count = cbl.UpdateViewCnt()
        update_view_count.run(card)

"""
A test class for RetrieveCardById

Jaco Koekemoer
2023-04-27
"""
class RetrieveCardByIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        id = 26

        card = cbl.Card()
        card.set_id(id)

        # Run the test
        retrieve_card = cbl.RetrieveCardById()
        card = retrieve_card.run(id)

        # Assert result
        ut.TestCase.assertFalse(card, None)
        print("ID: {:d}".format(card.get_id()))
        print("Title: {:s}".format(card.get_title()))
        print("Front: {:s}".format(card.get_front_content()))
        print("Back: {:s}".format(card.get_back_content()))
        print("Stack Id: {:d}".format(card.get_stack_id()))
        print("View Count: {:d}".format(card.get_view_count()))
        print("Group_Cd: {:d}".format(card.get_group_cd()))
        print("Active: {}".format(card.get_active()))
        print("Last View Date: {}".format(card.get_last_view_date()))
        print(type(card))

"""
A test class for RetrieveAllCards

Jaco Koekemoer
2023-04-27
"""
class RetrieveAllCardsTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Run the test
        retrieve_all_cards = cbl.RetrieveAllCards()
        cards = retrieve_all_cards.run()

        for card in cards:
            print(card)

"""
A test class for RetrieveAllActiveCardsByStackId

Jaco Koekemoer
2023-04-27
"""
class RetrieveActiveCardsByStackIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameter
        stack_id = 2

        # Run the test
        retrieve_cards = cbl.RetrieveActiveCardsByStackId()
        cards = retrieve_cards.run(stack_id)

        for card in cards:
            print(card)

"""
A test class for UpdateViewStatistics

Jaco Koekemoer
2023-04-27
"""
class UpdateViewStatisticsTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameter
        card_id = 26

        # Run the test
        update_view_statistics = cbl.UpdateViewStatistics()
        update_view_statistics.run(card_id)

"""
A unit test for UpdateCardGroup

Jaco Koekemoer
2023-04-27
"""
class UpdateCardGroupTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Prepare parameters
        card_id = 26
        group_cd = cc.CardGroup.MIDDLE.value

        # Run the test
        update_card_group = cbl.UpdateCardGroup()
        update_card_group.run(card_id, group_cd)

# Run all tests
# ut.main()

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddCardTest)
# suite = loader.loadTestsFromTestCase(UpdateCardTest)
# suite = loader.loadTestsFromTestCase(UpdateViewCntTest)
# suite = loader.loadTestsFromTestCase(RetrieveCardByIdTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllCardsTest)
# suite = loader.loadTestsFromTestCase(RetrieveActiveCardsByStackIdTest)
# suite = loader.loadTestsFromTestCase(UpdateViewStatisticsTest)
suite = loader.loadTestsFromTestCase(UpdateCardGroupTest)

runner = ut.TextTestRunner()
runner.run(suite)

