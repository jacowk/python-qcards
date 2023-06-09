import unittest as ut
import card_dao as cd
import card_constant as cc
import csv  # https://docs.python.org/3/library/csv.html

class AddCardDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        title = "Test title 1"
        front_content = "Test Front 1"
        back_content = "Test Front 2"
        stack_id = 1
        active = 1

        add_card = cd.AddCardDAO()
        add_card.run(title, front_content, back_content, stack_id, active)


class AddMultipleCardsDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Read from a file, and loop to insert
        # filename = "card_imports/creational_design_patterns.csv"
        # filename = "card_imports/structural_design_patterns.csv"
        filename = "card_imports/behavioral_design_patterns.csv"
        # filename = "card_imports/test_import.csv"

        print ("Importing {:s}".format(filename))
        stack_id = int(input("Enter the stack id: "))

        # Import csv
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
                #stack_id = 1
                active = 1

                print(title, front_content, back_content, stack_id, active)

                add_card = cd.AddCardDAO()
                add_card.run(title, front_content, back_content, stack_id, active)


class RetrieveActiveCardsByStackIdDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        stack_id = 1

        # Run the test
        retrieve_cards = cd.RetrieveActiveCardsByStackIdDAO()
        results = retrieve_cards.run(stack_id, True, True)

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        for result in results:
            print(result)


class UpdateViewStatisticsDAOTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        card_id = 1

        # Run the test
        update_stats = cd.UpdateViewStatisticsDAO()
        update_stats.run(card_id)

class UpdateCardGroupTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        card_id = 2
        group_cd = cc.CardGroup.MIDDLE.value

        # Run the test
        update_card_group = cd.UpdateCardGroupDAO()
        update_card_group.run(card_id, group_cd)

# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddCardDAOTest)
suite = loader.loadTestsFromTestCase(AddMultipleCardsDAOTest)
# suite = loader.loadTestsFromTestCase(RetrieveActiveCardsByStackIdDAOTest)
# suite = loader.loadTestsFromTestCase(UpdateViewStatisticsTest)
# suite = loader.loadTestsFromTestCase(UpdateCardGroupTest)

runner = ut.TextTestRunner()
runner.run(suite)
