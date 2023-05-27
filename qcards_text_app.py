from os import system
import category_dao as mc
import stack_dao as ms
import card_dao as mcard

"""
The main class that runs the text based application

Jaco Koekemoer
2023-04-07
"""
class QCardsTextApp:

    def run(self):
        # Run in a loop
        while True:
            # Clear the screen
            system('clear')

            # Retrieve all categories
            retrieve_active_categories = mc.RetrieveAllActiveCategories()
            active_categories = retrieve_active_categories.run()

            # Request a category selection
            # Loop through categories
            for active_category in active_categories:
                print("{:d}) {:s}".format(active_category[0], active_category[1]))

            category_id = input("\nEnter the number of the category you want to review: ")
            selected_category_name = active_categories[category_id][1]

            # Retrieve active stacks by category id
            retrieve_active_stacks = ms.RetrieveActiveStacksByCategoryId()
            active_stacks = retrieve_active_stacks.run(int(category_id))

            # Request a stack selection
            # Loop through stacks
            for active_stack in active_stacks:
                print("{:d}) {:s}".format(active_stack[0], active_stack[1]))

            stack_id = input("\nEnter the number of the stack you want to review: ")
            selected_stack_name = active_stacks[stack_id][1]

            print("Stack selected: {:s}".format(stack_id))

            # Retrieve the cards by stack id
            retrieve_active_cards = mcard.RetrieveAllActiveCardsByStackId()
            active_cards = retrieve_active_cards.run(int(stack_id))
            total = len(active_cards)
            count = 0

            # Loop through active cards
            for active_card in active_cards:
                count += 1

                # Clear the screen
                system('clear')

                # Get the csv fields
                id = active_card[0]
                title = active_card[1]
                front_content = active_card[2]
                back_content = active_card[3]

                # Create output
                print("Category: {:s}".format(selected_category_name))
                print("Stack: {:s}".format(selected_stack_name))
                print("Card Id: {:d} ({:d} of {:d})\nTitle: {:s}\nFront:\n{:s}".format(id, count, total, title, front_content))
                input("\nPress any key to view the back")
                print("\nBack:\n{:s}".format(back_content))
                update_view_statistics = mcard.UpdateViewStatistics()
                update_view_statistics.run(id)
                response = input("\nPress e to exit, or any other key to go to the next card. ")

                if response == 'e':
                    break

            # Request the user if they want to continue
            continue_review = input("\nDo you want to continue? (y/n) ")
            if continue_review == "n":
                break

qcards_text_app = QCardsTextApp()
qcards_text_app.run()
