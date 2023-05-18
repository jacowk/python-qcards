import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as messagebox
import card_bl as cbl
import qcards_gui_util as u
import qcards_util as qu
import category_bl as catbl
import category_constant as catc
import stack_bl as sbl
import stack_constant as sc

"""
Description: A class for listing cards
Author: Jaco Koekemoer
Date: 2023-04-27
"""
class ListCardsGui:

    def __init__(self, main_window):
        self.card_window = tk.Toplevel(main_window)
        # With transient(), the card_window will always be displayed on top of the main window
        self.card_window.transient(main_window)
        # Calculate the position of the center of the screen
        self.calculate_screen_position(1200, 500)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Define a Category Frame above the table
        self.stack_filter_frame = tk.Frame(self.card_window)
        self.stack_filter_frame.grid(row=0, column=0, columnspan=2)

        # Add a category filter dropdown
        self.category_filter_label = ttk.Label(self.stack_filter_frame, text="Category:")
        self.category_filter_label.grid(column=0, row=0, sticky="w")
        self.category_filter_dict = self.populate_categories()
        self.category_filter_combobox = ttk.Combobox(self.stack_filter_frame, values=list(self.category_filter_dict.keys()), width=40)
        self.category_filter_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.category_filter_combobox.current(0)
        self.selected_category_filter_id = None

        # Bind the function to the Combobox selection event
        self.category_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Add a stack filter dropdown
        self.stack_filter_label = ttk.Label(self.stack_filter_frame, text="Stack:")
        self.stack_filter_label.grid(column=2, row=0, sticky="w")
        self.stack_filter_combobox = ttk.Combobox(self.stack_filter_frame, width=40)
        self.stack_filter_combobox.grid(column=3, row=0, sticky="w", pady=(1, 2))
        self.selected_stack_filter_id = None

        # Bind the function to the Combobox selection event
        self.stack_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_stack())

        # Define the columns
        columns = ('id', 'category', 'stack', 'summary', 'front_content', 'last_view_date', 'active')

        # Create a TreeView (Table)
        self.tree = ttk.Treeview(self.card_window, columns=columns, show='headings')

        # Define the headings
        self.tree.heading('id', text="ID")
        self.tree.heading('category', text="Category")
        self.tree.heading('stack', text="Stack")
        self.tree.heading('summary', text="Summary")
        self.tree.heading('front_content', text="Front")
        self.tree.heading('last_view_date', text="Last View Date")
        self.tree.heading('active', text="Active")

        # Change column widths
        self.tree.column("id", anchor=tk.CENTER, stretch=tk.NO, width=90)
        self.tree.column("active", anchor=tk.CENTER, stretch=tk.NO, width=90)

        # Place the TreeView on the grid
        self.tree.grid(row=1, column=0, sticky='nsew')

        # Define a scrollbar
        scrollbar = ttk.Scrollbar(self.card_window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

        # Configure the row and column weights
        self.card_window.rowconfigure(1, weight=1)
        self.card_window.columnconfigure(0, weight=1)

        # Define a button Frame below the table
        self.button_frame = tk.Frame(self.card_window)
        self.button_frame.grid(row=2, column=0, columnspan=2)

        # Add buttons
        add_card_button = ttk.Button(self.button_frame, text="Add Card", command=self.add_card)
        add_card_button.grid(row=0, column=0, pady=(2, 2))
        update_card_button = ttk.Button(self.button_frame, text="Update Card", command=self.update_card)
        update_card_button.grid(row=0, column=1, pady=(2, 2))
        refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh_table)
        refresh_button.grid(row=0, column=2, pady=(2, 2))
        close_button = tk.Button(self.button_frame, text="Close", command=self.card_window.destroy)
        close_button.grid(row=0, column=3, pady=(2, 2))

        # Populate the grid with data
        self.populate_cards()

        # Wait for the child window to be visible. wait_visibility() has to be called before grab_set
        self.card_window.wait_visibility()
        # With grab_set(), give the card_window focus, and prevent the main_window from being clickable
        self.card_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.card_window.winfo_screenwidth(), self.card_window.winfo_screenheight())
        self.card_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def populate_cards(self, stack_filter_id = None):
        all_cards = []
        if stack_filter_id == None or stack_filter_id == -1:
            retrieve_all_cards = cbl.RetrieveAllCards()
            all_cards = retrieve_all_cards.run()
        else:
            # Retrieve cards by stack_filter_id
            retrieve_cards_by_stack_id = cbl.RetrieveActiveCardsByStackId()
            all_cards = retrieve_cards_by_stack_id.run(stack_filter_id)
        for card in all_cards:
            # id, summary, front_content, back_content, stack_id, view_count, group_cd, active, last_view_date
            values = (card[0], card[10], card[9], card[1], card[2], card[8], card[7])
            self.tree.insert('', tk.END, values=values)
        self.card_window.title("List Cards ({} cards)".format(len(all_cards)))

    def add_card(self):
        add_card_gui = AddCardGui(self.card_window, self, self.selected_category, self.selected_stack)

    def update_card(self):
        # Get values
        selected_item = self.tree.focus()

        # If no selection was made, display an error message
        if len(selected_item) == 0:
            messagebox.showerror("Error", "Please select a card to update")
            return

        # Current_item is a dictionary
        current_item = self.tree.item(selected_item)

        # Get the values index from the dictionary, which contains a list
        values = current_item['values']

        # Each item in the list corresponds with the columns in the TreeView
        id = values[0]

        # Retrieve the card from the database
        retrieve_card = cbl.RetrieveCardById()
        card = retrieve_card.run(id)

        # Run the update GUI
        update_card_gui = UpdateCardGui(self.card_window, self, card)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_cards(self.selected_stack_filter_id)

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_category(self):
        # Get teh selected category
        self.selected_category = self.category_filter_combobox.get()
        self.selected_category_filter_id = self.category_filter_dict[self.selected_category]

        # Retrieve all stacks
        retrieve_all_stacks = sbl.RetrieveStacksByCategoryIdDict()
        self.stack_filter_dict = retrieve_all_stacks.run(self.selected_category_filter_id)

        # Clear the stack dropdown
        self.stack_filter_combobox.delete(0, tk.END)

        # Populate the stack dropdown
        self.stack_filter_combobox['values'] = list(self.stack_filter_dict.keys())
        self.stack_filter_combobox.current(0)

    # Define a function to get the selected value from the dictionary
    def get_selected_stack(self):
        # Get the selected stack
        self.selected_stack = self.stack_filter_combobox.get()
        self.selected_stack_filter_id = self.stack_filter_dict[self.selected_stack]

        # Clear the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve cards by selected stack id
        self.populate_cards(self.selected_stack_filter_id)

"""
Description: A class for adding a card
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class AddCardGui:

    def __init__(self, card_window, list_cards_gui, main_selected_category = None, main_selected_stack = None):
        self.list_cards_gui = list_cards_gui
        self.card_window = card_window
        self.main_selected_category = main_selected_category
        self.main_selected_stack = main_selected_stack
        self.add_card_window = tk.Toplevel(self.card_window)
        self.add_card_window.transient(self.card_window)
        self.add_card_window.title("Add Card")
        self.add_card_window.resizable(False, False)

        self.frame = tk.Frame(self.add_card_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(620, 630)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Add a category filter dropdown
        self.category_filter_label = ttk.Label(self.frame, text="Category:")
        self.category_filter_label.grid(column=0, row=0, sticky="w")
        self.category_filter_dict = self.populate_categories()
        self.category_filter_combobox = ttk.Combobox(self.frame,
                                                     values=list(self.category_filter_dict.keys()), width=61)
        self.category_filter_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        if self.main_selected_category is None:
            self.category_filter_combobox.current(0)
            self.selected_category_filter_id = None
        else:
            # Prepopulate the category if a value was passed from the parent window
            self.category_filter_combobox.set(self.main_selected_category)
            #print(self.category_filter_dict)
            #print(self.main_selected_category)
            self.selected_category_filter_id = self.category_filter_dict[self.main_selected_category]

        # Bind the function to the Combobox selection event
        self.category_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Stack dropdown
        self.stack_label = ttk.Label(self.frame, text="Stack:")
        self.stack_label.grid(column=0, row=1, sticky="w")
        self.stack_combobox = ttk.Combobox(self.frame, width=61)
        self.stack_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))
        if self.main_selected_stack is None:
            self.selected_stack_id = None
        else:
            # Prepopulate the stack if a value was passed from the parent window
            # Retrieve all stacks
            retrieve_all_stacks = sbl.RetrieveStacksByCategoryIdDict()
            self.stack_dict = retrieve_all_stacks.run(self.selected_category_filter_id)
            self.selected_stack_id = self.stack_dict[self.main_selected_stack]

            # Populate the stack dropdown
            self.stack_combobox['values'] = list(self.stack_dict.keys())
            self.stack_combobox.set(self.main_selected_stack)


        # Bind the function to the Combobox selection event
        self.stack_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_stack())

        # Summary field
        self.summary_label = ttk.Label(self.frame, text="Summary:")
        self.summary_label.grid(column=0, row=2, sticky="w")
        self.summary_entry = ttk.Entry(self.frame, width=61)
        self.summary_entry.grid(column=1, row=2, sticky="w", pady=(1, 2))

        # Front field
        self.front_label = ttk.Label(self.frame, text="Front:")
        self.front_label.grid(column=0, row=3, sticky="w")
        font_name = "Courier New"
        font_size = 10
        self.front_content_text = scrolledtext.ScrolledText(self.frame,
                                                            width=61,
                                                            height=14,
                                                            padx=5,
                                                            pady=5,
                                                            font=(font_name, font_size),
                                                            wrap="word")
        self.front_content_text.grid(column=1, row=3, sticky="w", pady=(1, 1))

        # Back field
        self.back_content_label = ttk.Label(self.frame, text="Back:")
        self.back_content_label.grid(column=0, row=4, sticky="w")
        font_name = "Courier New"
        font_size = 10
        self.back_content_text = scrolledtext.ScrolledText(self.frame,
                                                           width=61,
                                                           height=14,
                                                           padx=5,
                                                           pady=5,
                                                           font=(font_name, font_size),
                                                           wrap="word")
        self.back_content_text.grid(column=1, row=4, sticky="w", pady=(1, 2))

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:")
        self.active_label.grid(column=0, row=5, sticky="w")
        self.active_var = tk.BooleanVar()
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=5, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=6, columnspan=2)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_card)
        self.add_button.grid(column=0, row=0, pady=(1, 2))
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.add_card_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=(1, 2))

        self.set_tab_order()
        self.add_card_window.wait_visibility()
        self.add_card_window.grab_set()

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    def get_selected_category(self):
        # Get teh selected category
        selected_category = self.category_filter_combobox.get()
        self.selected_category_filter_id = self.category_filter_dict[selected_category]

        # Retrieve all stacks
        retrieve_all_stacks = sbl.RetrieveStacksByCategoryIdDict()
        self.stack_dict = retrieve_all_stacks.run(self.selected_category_filter_id)

        # Clear the stack dropdown
        self.stack_combobox.delete(0, tk.END)

        # Populate the stack dropdown
        self.stack_combobox['values'] = list(self.stack_dict.keys())
        self.stack_combobox.current(0)

    def populate_stacks(self):
        retrieve_all_stacks = sbl.RetrieveAllStacksDict()
        return retrieve_all_stacks.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_stack(self):
        selected_stack = self.stack_combobox.get()
        self.selected_stack_id = self.stack_dict[selected_stack]

    def add_card(self):
        # summary, front_content, back_content, stack_id, active
        summary = self.summary_entry.get()
        #front_content = self.front_content_entry.get()
        front_content = self.front_content_text.get("1.0", tk.END)
        back_content = self.back_content_text.get("1.0", tk.END)
        qcards_util = qu.QCardsUtil()
        stack_id = qcards_util.get_selected_combobox_value(self.selected_stack_id)
        active = self.active_var.get()

        # Prepare Card
        card = cbl.Card()
        card.set_summary(summary)
        card.set_front_content(front_content)
        card.set_back_content(back_content)
        card.set_stack_id(stack_id)
        card.set_active(active)

        # Store the new Card in a database
        add_card = cbl.AddCard()
        add_card.run(card)

        # Add the card to the card tree view
        #self.card_window.tree.insert("", "end", text=desc, values=(active,))
        self.list_cards_gui.refresh_table()

        # Show message
        #messagebox.showinfo("Card added", f"{description} added to cards.")

        # Close the form
        self.add_card_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.add_card_window.winfo_screenwidth(), self.add_card_window.winfo_screenheight())
        self.add_card_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def set_tab_order(self):
        self.category_filter_combobox.lift()
        self.stack_combobox.lift()
        self.summary_entry.lift()
        self.front_content_text.lift()
        self.back_content_label.lift()
        self.active_checkbutton.lift()
        self.add_button.lift()
        self.cancel_button.lift()

"""
Description: A class for updating a card
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class UpdateCardGui:

    def __init__(self, card_window, list_cards_gui, card):
        self.list_cards_gui = list_cards_gui
        self.card_window = card_window
        self.update_card_window = tk.Toplevel(self.card_window)
        self.update_card_window.transient(self.card_window)
        self.update_card_window.title("Update Card")
        self.update_card_window.resizable(False, False)

        self.frame = tk.Frame(self.update_card_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(620, 650)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Populate the update window with the selected item's values
        self.id_var = tk.IntVar(value=card.get_id())
        self.summary_var = tk.StringVar(value=card.get_summary())
        self.front_content_var = card.get_front_content()
        self.back_content_var = card.get_back_content()
        self.active_var = tk.BooleanVar(value=card.get_active())
        self.last_view_date_var = card.get_last_view_date() if card.get_last_view_date() is not None else ""

        # Id field
        self.id_label = ttk.Label(self.frame, text="ID:")
        self.id_label.grid(column=0, row=0, sticky="w")
        self.id_label = ttk.Label(self.frame, textvariable=self.id_var)
        self.id_label.grid(column=1, row=0, sticky="w")

        # Category dropdown
        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(column=0, row=1, sticky="w")
        # Load the dictionary for the combobox
        self.category_dict = self.populate_categories()

        # Preselect the combobox with the appropriate value
        qcards_util = qu.QCardsUtil()
        self.selected_category = qcards_util.get_dictionary_key_from_value(self.category_dict, card.get_category_id())
        self.selected_category = catc.CategoryConstants.SELECT_CATEGORY.value if self.selected_category is None else self.selected_category
        self.selected_category_id = card.get_category_id()

        # The values are the keys of the dictionary of stacks, which contains the descriptions of the stacks
        self.category_combobox = ttk.Combobox(self.frame, textvariable=self.selected_category, values=list(self.category_dict.keys()), width=61)
        self.category_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))
        self.category_combobox.set(self.selected_category)

        # Bind the function to the Combobox selection event
        self.category_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Stack dropdown
        self.stack_label = ttk.Label(self.frame, text="Stack:")
        self.stack_label.grid(column=0, row=2, sticky="w")
        # Load the dictionary for the combobox
        self.stack_dict = self.populate_stacks()

        # Preselect the combobox with the appropriate value
        qcards_util = qu.QCardsUtil()
        self.selected_stack = qcards_util.get_dictionary_key_from_value(self.stack_dict, card.get_stack_id())
        self.selected_stack = sc.StackConstant.SELECT_STACK.value if self.selected_stack is None else self.selected_stack
        self.selected_stack_id = card.get_stack_id()

        # The values are the keys of the dictionary of cards, which contains the descriptions of the cards
        self.stack_combobox = ttk.Combobox(self.frame, textvariable=self.selected_stack, values=list(self.stack_dict.keys()), width=61)
        self.stack_combobox.grid(column=1, row=2, sticky="w", pady=(1, 2))
        self.stack_combobox.set(self.selected_stack)

        # Bind the function to the Combobox selection event
        self.stack_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_stack())

        # Summary field
        self.summary_label = ttk.Label(self.frame, text="Summary:")
        self.summary_label.grid(column=0, row=3, sticky="w")
        self.summary_entry = ttk.Entry(self.frame, textvariable=self.summary_var, width=61)
        self.summary_entry.grid(column=1, row=3, sticky="w", pady=(1, 1))

        # Front field
        self.front_content_label = ttk.Label(self.frame, text="Front:")
        self.front_content_label.grid(column=0, row=4, sticky="w")

        font_name = "Courier New"
        font_size = 10
        self.front_content_text = scrolledtext.ScrolledText(self.frame,
                                                           width=61,
                                                           height=14,
                                                           padx=5,
                                                           pady=5,
                                                           font=(font_name, font_size),
                                                            wrap="word")
        self.front_content_text.insert(tk.END, self.front_content_var)
        self.front_content_text.grid(column=1, row=4, sticky="w", pady=(1, 1))

        # Back field
        self.back_content_label = ttk.Label(self.frame, text="Back:")
        self.back_content_label.grid(column=0, row=5, sticky="w")
        self.back_content_text = scrolledtext.ScrolledText(self.frame,
                                                           width=61,
                                                           height=14,
                                                           padx=5,
                                                           pady=5,
                                                           font=(font_name, font_size),
                                                           wrap="word")
        self.back_content_text.insert(tk.END, self.back_content_var)
        self.back_content_text.grid(column=1, row=5, sticky="w", pady=(1, 1))

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:", anchor='w')
        self.active_label.grid(column=0, row=6, sticky="w")
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=6, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=7, columnspan=2)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_card)
        self.save_button.grid(column=0, row=0, pady=(2, 2))
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.update_card_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=(2, 2))

        self.update_card_window.wait_visibility()
        self.update_card_window.grab_set()

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    def get_selected_category(self):
        # Get th selected category
        self.selected_category = self.category_combobox.get()
        self.selected_category_id = self.category_dict[self.selected_category]

        # Retrieve all stacks
        retrieve_all_stacks = sbl.RetrieveStacksByCategoryIdDict()
        self.stack_dict = retrieve_all_stacks.run(self.selected_category_id)

        # Clear the stack dropdown
        self.stack_combobox.delete(0, tk.END)

        # Populate the stack dropdown
        self.stack_combobox['values'] = list(self.stack_dict.keys())
        self.stack_combobox.current(0)

    def populate_stacks(self):
        retrieve_all_stacks = sbl.RetrieveAllStacksDict()
        return retrieve_all_stacks.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_stack(self):
        self.selected_stack = self.stack_combobox.get()
        self.selected_stack_id = self.stack_dict[self.selected_stack]

    def save_card(self):
        id = self.id_var.get()
        summary = self.summary_entry.get()
        front_content = self.front_content_text.get("1.0", tk.END)
        back_content = self.back_content_text.get("1.0", tk.END)
        qcards_util = qu.QCardsUtil()
        stack_id = qcards_util.get_selected_combobox_value(self.selected_stack_id)
        active = self.active_var.get()

        # Prepare Card
        card = cbl.Card()
        card.set_id(id)
        card.set_summary(summary)
        card.set_front_content(front_content)
        card.set_back_content(back_content)
        card.set_stack_id(stack_id)
        card.set_active(active)

        # Store the new Card in a database
        persist_card = cbl.UpdateCard()
        persist_card.run(card);

        # Update the card to the card tree view
        selected_item = self.list_cards_gui.tree.focus()
        self.list_cards_gui.tree.item(selected_item, values=(id,
                                                             self.selected_category,
                                                             self.selected_stack,
                                                             summary,
                                                             front_content,
                                                             self.last_view_date_var,
                                                             active))

        # Close the form
        self.update_card_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.update_card_window.winfo_screenwidth(), self.update_card_window.winfo_screenheight())
        self.update_card_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))
