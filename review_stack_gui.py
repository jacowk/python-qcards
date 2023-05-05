import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.messagebox as messagebox
import stack_bl as sbl
import card_bl as cbl
import review_stage_gui as rsg
import review_stage_bl as rsbl
import qcards_gui_util as u
import qcards_util as qu
import category_bl as catbl
import qcards_date_util as qdu

"""
Description: A class for seeing all stacks that should be reviewed today
Author: Jaco Koekemoer
Date: 2023-04-27
"""
class ReviewGui:

    def __init__(self, main_window):
        self.stack_window = tk.Toplevel(main_window)
        # With transient(), the stack_window will always be displayed on top of the main window
        self.stack_window.transient(main_window)
        self.stack_window.title("Review Stacks")
        # Calculate the position of the center of the screen
        self.calculate_screen_position(1000, 500)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Define the columns
        # stack_id, stack, category, review_stage_cd, next_view_date
        columns = ('stack_id', 'stack', 'category', 'review_stage', 'next_view_date')

        # Define a current date Frame above the table
        self.current_date_frame = tk.Frame(self.stack_window)
        self.current_date_frame.grid(row=0, column=0, columnspan=2)
        self.current_date_label = ttk.Label(self.current_date_frame, text="Today's Date:")
        self.current_date_label.grid(column=0, row=0, sticky="w")
        self.current_date = ttk.Label(self.current_date_frame, text=qdu.DateUtil.get_now_as_year_month_day())
        self.current_date.grid(column=1, row=0, sticky="w")

        # Create a TreeView (Table)
        self.tree = ttk.Treeview(self.stack_window, columns=columns, show='headings')

        # Define the headings
        self.tree.heading('stack_id', text="Stack ID")
        self.tree.heading('stack', text="Stack")
        self.tree.heading('category', text="Category")
        self.tree.heading('review_stage', text="Review Stage")
        self.tree.heading('next_view_date', text="Next View Date")

        # Change column widths
        self.tree.column("stack_id", anchor=tk.CENTER, stretch=tk.NO, width=90)

        # Place the TreeView on the grid
        self.tree.grid(row=1, column=0, sticky='nsew')

        # Define a scrollbar
        scrollbar = ttk.Scrollbar(self.stack_window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

        # Configure the row and column weights
        self.stack_window.rowconfigure(1, weight=1)
        self.stack_window.columnconfigure(0, weight=1)

        # Define a button Frame below the table
        self.button_frame = tk.Frame(self.stack_window)
        self.button_frame.grid(row=2, column=0, columnspan=2)

        # Add buttons
        review_stack_button = ttk.Button(self.button_frame, text="Review Stack", command=self.review_stack)
        review_stack_button.grid(row=1, column=0, padx=5, pady=(2, 2))
        review_stage_button = tk.Button(self.button_frame, text="Update Review Stage", command=self.update_review_stage)
        review_stage_button.grid(row=1, column=1, pady=(2, 2))
        calculate_next_view_date_button = ttk.Button(self.button_frame, text="Calc Next View Date", command=self.calculate_next_view_date)
        calculate_next_view_date_button.grid(row=1, column=2, pady=(2, 2))
        refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh_table)
        refresh_button.grid(row=1, column=3, padx=5, pady=(2, 2))
        close_button = tk.Button(self.button_frame, text="Close", command=self.stack_window.destroy)
        close_button.grid(row=1, column=4, padx=5, pady=(2, 2))

        # Populate the grid with data
        self.populate_stacks_for_review()

        # Wait for the child window to be visible. wait_visibility() has to be called before grab_set
        self.stack_window.wait_visibility()
        # With grab_set(), give the stack_window focus, and prevent the main_window from being clickable
        self.stack_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.stack_window.winfo_screenwidth(), self.stack_window.winfo_screenheight())
        self.stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def populate_stacks_for_review(self):
        retrieve_stacks_for_review = sbl.RetrieveStacksForReview()
        stacks_for_review = retrieve_stacks_for_review.run()
        for stack in stacks_for_review:
            # s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd, c.description, lrs.description
            # stack_id, stack, category, review_stage_cd, next_view_date, lrs.description
            values = (stack[0], stack[1], stack[7], stack[8], stack[5])
            self.tree.insert('', tk.END, values=values)

    """
    Open a screen to review the active cards for the selected stack
    """
    def review_stack(self):
        # Get values
        selected_item = self.tree.focus()

        # If no selection was made, display an error message
        if len(selected_item) == 0:
            messagebox.showerror("Error", "Please select a stack to review")
            return

        # Current_item is a dictionary
        current_item = self.tree.item(selected_item)

        # Get the values index from the dictionary, which contains a list
        values = current_item['values']

        # Each item in the list corresponds with the columns in the TreeView
        stack_id = values[0]

        # Retrieve the stack
        retrieve_stack_by_id = sbl.RetrieveStackById()
        stack = retrieve_stack_by_id.run(stack_id)
        stack.set_id(stack_id)

        # Retrieve all the cards for the stack to review, to be passed on to ReviewStackGui
        retrieve_cards_by_stack_id = cbl.RetrieveActiveCardsByStackId()
        cards_for_review = retrieve_cards_by_stack_id.run(stack_id)

        # Open the review gui
        review_stack_gui = ReviewStackGui(self.stack_window, stack, cards_for_review)

    """
    Open a screen to view and update a stack's review stage
    """
    def update_review_stage(self):
        # Get values
        selected_item = self.tree.focus()

        # If no selection was made, display an error message
        if len(selected_item) == 0:
            messagebox.showerror("Error", "Please select a stack to view it's review stage")
            return

        # Current_item is a dictionary
        current_item = self.tree.item(selected_item)

        # Get the values index from the dictionary, which contains a list
        values = current_item['values']

        # Each item in the list corresponds with the columns in the TreeView
        stack_id = values[0]

        # Retrieve the stack
        retrieve_stack_by_id = sbl.RetrieveStackById()
        stack = retrieve_stack_by_id.run(stack_id)
        stack.set_id(stack_id)

        # Retrieve the review stage
        retrieve_review_stage_by_stack_id = rsbl.RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage_by_stack_id.run(stack_id)

        # Open Review Stage screen
        review_stage_gui = rsg.ReviewStageGui(self.stack_window, stack, review_stage)

    def calculate_next_view_date(self):
        # Get values
        selected_item = self.tree.focus()

        # If no selection was made, display an error message
        if len(selected_item) == 0:
            messagebox.showerror("Error", "Please select a stack to update")
            return

        # Current_item is a dictionary
        current_item = self.tree.item(selected_item)

        # Get the values index from the dictionary, which contains a list
        values = current_item['values']

        # Each item in the list corresponds with the columns in the TreeView
        stack_id = values[0]

        # Calculate and update the next view date
        calc_update_next_view_date = rsbl.CalculateAndUpdateNextViewDate()
        next_view_date = calc_update_next_view_date.run(stack_id)

        self.refresh_table()
        if next_view_date is not None:
            messagebox.showinfo("Calculate Next View Date", "Next view date calculated: {:%Y-%m-%d}".format(next_view_date))
        else:
            messagebox.showinfo("Calculate Next View Date", "No next view date calculated")

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_stacks_for_review()

"""
Description: A class for reviewing the cards for a stack that is scheduled for review
Author: Jaco Koekemoer
Date: 2023-04-28
"""
class ReviewStackGui:

    def __init__(self, main_review_list_window, stack, cards_for_review):
        self.main_review_list_window = main_review_list_window
        self.stack = stack
        self.cards_for_review = cards_for_review
        self.review_stack_window = tk.Toplevel(self.main_review_list_window)
        self.review_stack_window.transient(self.main_review_list_window)
        self.review_stack_window.title("Review Cards")
        self.review_stack_window.resizable(False, False)

        self.frame = tk.Frame(self.review_stack_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(810, 380)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Define the initial index of the list of cards for review. cards_for_review is a tuple, and we start at index 0
        # As the user clicks Next, we increment this variable with 1 to get the next card to review
        self.card_review_index = 0

        # Get the initial card for review
        card_for_review = self.cards_for_review[self.card_review_index]

        # Set initial fields
        self.id_var = tk.IntVar(value=card_for_review[0])
        self.summary_var = tk.StringVar(value=card_for_review[1])
        self.front_content_var = tk.StringVar(value=card_for_review[2])
        self.back_content_var = card_for_review[3]
        self.current_view_count_var = tk.IntVar(value=card_for_review[5])
        self.last_view_date_var = tk.StringVar(value=card_for_review[8])
        self.stack_description_var = tk.StringVar(value=card_for_review[9])
        self.category_description_var = tk.StringVar(value=card_for_review[10])
        self.view_count_var = tk.IntVar(value=card_for_review[5])
        self.last_view_date_var = tk.StringVar(value=card_for_review[8])

        # Id field
        self.id_label = ttk.Label(self.frame, text="ID:")
        self.id_label.grid(column=0, row=0, sticky="w")
        self.id_label = ttk.Entry(self.frame, textvariable=self.id_var, width=20,state="readonly")
        self.id_label.grid(column=1, row=0, sticky="w")

        # Category field
        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(column=0, row=1, sticky="w")
        self.category_entry = ttk.Entry(self.frame, textvariable=self.category_description_var, width=80, state="readonly")
        self.category_entry.grid(column=1, row=1, sticky="w", pady=(1, 1))

        # Stack field
        self.category_label = ttk.Label(self.frame, text="Stack:")
        self.category_label.grid(column=0, row=2, sticky="w")
        self.category_entry = ttk.Entry(self.frame, textvariable=self.stack_description_var, width=80,
                                        state="readonly")
        self.category_entry.grid(column=1, row=2, sticky="w", pady=(1, 1))

        # Summary field
        self.summary_label = ttk.Label(self.frame, text="Summary:")
        self.summary_label.grid(column=0, row=3, sticky="w")
        self.summary_entry = ttk.Entry(self.frame, textvariable=self.summary_var, width=80, state="readonly")
        self.summary_entry.grid(column=1, row=3, sticky="w", pady=(1, 1))

        # Front field
        self.front_content_label = ttk.Label(self.frame, text="Front:")
        self.front_content_label.grid(column=0, row=4, sticky="w")
        self.front_content_entry = ttk.Entry(self.frame, textvariable=self.front_content_var, width=80, state="readonly")
        self.front_content_entry.grid(column=1, row=4, sticky="w", pady=(1, 1))

        # Back field
        self.back_content_label = ttk.Label(self.frame, text="Back:")
        self.back_content_label.grid(column=0, row=5, sticky="w")
        font_name = "Courier New"
        font_size = 10
        self.back_content_text = scrolledtext.ScrolledText(self.frame,
                                                           width=80,
                                                           height=8,
                                                           padx=5,
                                                           pady=5,
                                                           font=(font_name, font_size),
                                                           wrap="word")
        self.back_content_text.insert("1.0", self.back_content_var)
        self.back_content_text.grid(column=1, row=5, sticky="w", pady=(1, 1))

        # Configure the tags to change the font color
        self.back_content_text.tag_configure("white", foreground="white")
        self.back_content_text.tag_configure("black", foreground="black")

        # Set initial color to white, to hide the back text
        self.back_content_text.tag_add("white", "1.0", tk.END)

        # View count field
        self.view_count_label = ttk.Label(self.frame, text="View Count:")
        self.view_count_label.grid(column=0, row=6, sticky="w")
        self.view_count_entry = ttk.Entry(self.frame, textvariable=self.view_count_var, width=80,
                                             state="readonly")
        self.view_count_entry.grid(column=1, row=6, sticky="w", pady=(1, 1))

        # Last view date field
        self.last_view_date_label = ttk.Label(self.frame, text="Last View Date:")
        self.last_view_date_label.grid(column=0, row=7, sticky="w")
        self.last_view_date_entry = ttk.Entry(self.frame, textvariable=self.last_view_date_var, width=80,
                                          state="readonly")
        self.last_view_date_entry.grid(column=1, row=7, sticky="w", pady=(1, 1))

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=8, columnspan=2)

        # Buttons
        restart_button = tk.Button(self.button_frame, text="Restart", command=self.restart)
        restart_button.grid(column=0, row=0, pady=(2, 2))
        previous_card_button = tk.Button(self.button_frame, text="Previous Card", command=self.previous_card)
        previous_card_button.grid(column=1, row=0, pady=(2, 2))
        reveal_back_button = tk.Button(self.button_frame, text="Reveal Back", command=self.reveal_back_content)
        reveal_back_button.grid(column=2, row=0, pady=(2, 2))
        next_card_button = tk.Button(self.button_frame, text="Next Card", command=self.next_card)
        next_card_button.grid(column=3, row=0, pady=(2, 2))
        close_button = tk.Button(self.button_frame, text="Close", command=self.review_stack_window.destroy)
        close_button.grid(column=5, row=0, pady=(2, 2))

        self.review_stack_window.wait_visibility()
        self.review_stack_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.review_stack_window.winfo_screenwidth(), self.review_stack_window.winfo_screenheight())
        self.review_stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def restart(self):
        # First update the view statistics for the current card
        update_view_statistics = cbl.UpdateViewStatistics()
        update_view_statistics.run(self.id_var.get())

        # Load the previous card
        self.card_review_index = 0

        # Get the card for review
        card_for_review = self.cards_for_review[self.card_review_index]
        self.reset_fields(card_for_review)

    def previous_card(self):
        # First update the view statistics for the current card
        update_view_statistics = cbl.UpdateViewStatistics()
        update_view_statistics.run(self.id_var.get())

        # Load the previous card
        self.card_review_index -= 1
        if self.card_review_index == -1:
            messagebox.showinfo("Information", "You are already at the beginning of the stack")
            self.card_review_index += 1
            return

        # Get the card for review
        card_for_review = self.cards_for_review[self.card_review_index]
        self.reset_fields(card_for_review)

    def reveal_back_content(self):
        # Reveal the back content again by changing the color to black
        self.back_content_text.tag_add("black", "1.0", tk.END)

    def next_card(self):
        # First update the view statistics for the current card
        update_view_statistics = cbl.UpdateViewStatistics()
        update_view_statistics.run(self.id_var.get())

        # Load the next card
        self.card_review_index += 1
        if self.card_review_index >= len(self.cards_for_review):
            messagebox.showinfo("Information", "No more cards to review")
            self.card_review_index -= 1
            return

        # Get the card for review
        card_for_review = self.cards_for_review[self.card_review_index]
        self.reset_fields(card_for_review)

    def reset_fields(self, card_for_review):
        # Populate the update window with the selected item's values
        self.id_var.set(card_for_review[0])
        self.summary_var.set(card_for_review[1])
        self.front_content_var.set(card_for_review[2])
        self.current_view_count_var.set(card_for_review[5])
        self.last_view_date_var.set(card_for_review[8])
        self.stack_description_var.set(card_for_review[9])
        self.category_description_var.set(card_for_review[10])
        self.view_count_var.set(card_for_review[5])
        self.last_view_date_var.set(card_for_review[8])

        # Update the back content ScrolledText
        self.back_content_var = card_for_review[3]
        self.back_content_text.delete("1.0", tk.END)
        self.back_content_text.insert(tk.END, self.back_content_var)

        # Hide the back content again by changing the color to white
        self.back_content_text.tag_add("white", "1.0", tk.END)

