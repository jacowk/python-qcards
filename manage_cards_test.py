import unittest as ut
import manage_cards as mcard
import qcards_date_util as qdu
import csv #https://docs.python.org/3/library/csv.html

class AddCardTest(ut.TestCase):

    def runTest(self):
        title = "Test Title 1"
        front_content = "Test Front 1"
        back_content = "Test Front 2"
        stack_id = 1
        active = 1

        date_util = qdu.DateUtil()
        next_view_date = date_util.getNowAsYearMonthDay()

        add_card = mcard.AddCard()
        add_card.run(title, front_content, back_content, stack_id, active, next_view_date)

class AddMultipleCardsTest(ut.TestCase):

    def runTest(self):
        # Read from a file, and loop to insert
        filename = "cards_import.csv"

        # Import csv
        with open(filename, newline = '') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            cnt = 1

            for row in datareader:
                if cnt == 1:
                    cnt += 1
                    continue #Skip first line with only column names

                title = row[0]
                front_content = row[1]
                back_content = row[2]
                stack_id = 1
                active = 1

                date_util = qdu.DateUtil()
                next_view_date = date_util.getNowAsYearMonthDay()
                print(next_view_date)

                add_card = mcard.AddCard()
                add_card.run(title, front_content, back_content, stack_id, active, next_view_date)

# Run specific tests
loader = ut.TestLoader()
#suite = loader.loadTestsFromTestCase(AddCardTest)
suite = loader.loadTestsFromTestCase(AddMultipleCardsTest)

runner = ut.TextTestRunner()
runner.run(suite)
