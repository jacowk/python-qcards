import unittest as ut
import manage_cards as mcard
import qcards_date_util as qdu
import csv  # https://docs.python.org/3/library/csv.html


class AddCardTest(ut.TestCase):

    @staticmethod
    def runTest():
        summary = "Test summary 1"
        front_content = "Test Front 1"
        back_content = "Test Front 2"
        stack_id = 1
        active = 1

        add_card = mcard.AddCard()
        add_card.run(summary, front_content, back_content, stack_id, active)


class AddMultipleCardsTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Read from a file, and loop to insert
        # filename = "card_imports/creational_design_patterns.csv"
        # filename = "card_imports/structural_design_patterns.csv"
        # filename = "card_imports/behavioral_design_patterns.csv"
        filename = "card_imports/test_import.csv"

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

                summary = row[0]
                front_content = row[1]
                back_content = row[2]
                #stack_id = 1
                active = 1

                print(summary, front_content, back_content, stack_id, active)

                add_card = mcard.AddCard()
                add_card.run(summary, front_content, back_content, stack_id, active)


class RetrieveAllActiveCardsByStackIdTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        stack_id = 1

        # Run the test
        retrieve_cards = mcard.RetrieveAllActiveCardsByStackId()
        result = retrieve_cards.run(stack_id)

        # Assert result
        # ut.TestCase.assertTrue(len(result) > 0)
        print(result)
        print(type(result))


class UpdateViewStatisticsTest(ut.TestCase):

    @staticmethod
    def runTest():
        # Setup parameter
        card_id = 1

        # Run the test
        update_stats = mcard.UpdateViewStatistics()
        update_stats.run(card_id)


# Run specific tests
loader = ut.TestLoader()
# suite = loader.loadTestsFromTestCase(AddCardTest)
suite = loader.loadTestsFromTestCase(AddMultipleCardsTest)
# suite = loader.loadTestsFromTestCase(RetrieveAllActiveCardsByStackIdTest)
# suite = loader.loadTestsFromTestCase(UpdateViewStatisticsTest)


runner = ut.TextTestRunner()
runner.run(suite)
