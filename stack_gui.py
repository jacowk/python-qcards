import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import stack_bl as sbl
import qcards_gui_util as u
import qcards_util as qu
import category_bl as catbl
import category_constant as catc
import review_stage_bl as rsbl
import review_stack_gui as rsg
import review_stage_gui as rstg
import card_bl as cbl

"""
Description: A class for listing stacks
Author: Jaco Koekemoer
Date: 2023-04-23
"""
class ListStacksGui:

    def __init__(self, main_window):
        self.stack_window = tk.Toplevel(main_window)
        # With transient(), the stack_window will always be displayed on top of the main window
        self.stack_window.transient(main_window)
        # Calculate the position of the center of the screen
        self.calculate_screen_position(1200, 500)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Define a Category Frame above the table
        self.category_filter_frame = tk.Frame(self.stack_window)
        self.category_filter_frame.grid(row=0, column=0, columnspan=2)

        # Add a category filter dropdown
        self.category_filter_label = ttk.Label(self.category_filter_frame, text="Category:")
        self.category_filter_label.grid(column=0, row=0, sticky="w")
        self.category_filter_dict = self.populate_categories()
        self.category_filter_combobox = ttk.Combobox(self.category_filter_frame, values=list(self.category_filter_dict.keys()), width=61)
        self.category_filter_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.category_filter_combobox.current(0)
        self.selected_category_filter_id = None

        # Bind the function to the Combobox selection event
        self.category_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Define the columns
        columns = ('id', 'description', 'category', 'next_view_date', 'review_stage_id', 'review_stage', 'active')

        # Create a TreeView (Table)
        self.tree = ttk.Treeview(self.stack_window, columns=columns, show='headings')

        # Define the headings
        self.tree.heading('id', text="ID")
        self.tree.heading('description', text="Description")
        self.tree.heading('category', text="Category")
        self.tree.heading('next_view_date', text="Next View Date")
        self.tree.heading('review_stage_id', text="Review Stage ID")
        self.tree.heading('review_stage', text="Review Stage")
        self.tree.heading('active', text="Active")

        # Change column widths
        self.tree.column("id", anchor=tk.CENTER, stretch=tk.NO, width=90)
        self.tree.column("active", anchor=tk.CENTER, stretch=tk.NO, width=90)

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
        add_stack_button = ttk.Button(self.button_frame, text="Add Stack", command=self.add_stack)
        add_stack_button.grid(row=0, column=0, pady=5)
        update_stack_button = ttk.Button(self.button_frame, text="Update Stack", command=self.update_stack)
        update_stack_button.grid(row=0, column=1, pady=5)
        setup_review_stage_button = ttk.Button(self.button_frame, text="Setup Review Stage", command=self.setup_review_stage)
        setup_review_stage_button.grid(row=0, column=2, pady=5)
        review_stage_button = tk.Button(self.button_frame, text="Update Review Stage", command=self.update_review_stage)
        review_stage_button.grid(row=0, column=3, pady=5)
        calculate_next_view_date_button = ttk.Button(self.button_frame, text="Calc Next View Date",command=self.calculate_next_view_date)
        calculate_next_view_date_button.grid(row=0, column=4, pady=5)
        review_stack_button = ttk.Button(self.button_frame, text="Review Stack",
                                                     command=self.review_stack)
        review_stack_button.grid(row=0, column=5, pady=5)
        refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh_table)
        refresh_button.grid(row=0, column=6, pady=5)
        close_button = tk.Button(self.button_frame, text="Close", command=self.stack_window.destroy)
        close_button.grid(row=0, column=7, pady=5)

        # Populate the grid with data
        self.populate_stacks()

        # Wait for the child window to be visible. wait_visibility() has to be called before grab_set
        self.stack_window.wait_visibility()
        # With grab_set(), give the stack_window focus, and prevent the main_window from being clickable
        self.stack_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.stack_window.winfo_screenwidth(), self.stack_window.winfo_screenheight())
        self.stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

    def populate_stacks(self, category_filter_id = None):
        # Clear the tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Populate the stacks
        all_stacks = []
        if category_filter_id == None or category_filter_id == -1:
            retrieve_all_stacks = sbl.RetrieveAllStacks()
            all_stacks = retrieve_all_stacks.run()
        else:
            # Retrieve stacks by category_filter_id
            retrieve_stacks_by_category_id = sbl.RetrieveActiveStacksByCategoryId()
            all_stacks = retrieve_stacks_by_category_id.run(category_filter_id)

        # Prepare columns
        for stack in all_stacks:
            values = (stack[0], stack[1], stack[6], stack[5], stack[7], stack[8], stack[2])
            self.tree.insert('', tk.END, values=values)

        self.stack_window.title("List Stacks ({} stacks)".format(len(all_stacks)))

    def add_stack(self):
        add_stack_gui = AddStackGui(self.stack_window, self, self.selected_category)

    def update_stack(self):
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
        id = values[0]

        # Retrieve the stack from the database
        retrieve_stack = sbl.RetrieveStackById()
        stack = retrieve_stack.run(id)

        # Run the update GUI
        update_stack_gui = UpdateStackGui(self.stack_window, self, stack, self.selected_category_filter_id)

    def setup_review_stage(self):
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

        # Create the first daily review stage
        setup_review_stage = rsbl.SetupInitialReviewStage()
        setup_review_stage.run(stack_id)

        self.refresh_table()
        messagebox.showinfo("Review Stage Setup", "Review stage setup is done")

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
        review_stage_gui = rstg.ReviewStageGui(self.stack_window, stack, review_stage)

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
        review_stack_gui = rsg.ReviewStackGui(self.stack_window, stack, cards_for_review)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_stacks(self.selected_category_filter_id)

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_category(self):
        # Get teh selected category
        self.selected_category = self.category_filter_combobox.get()
        self.selected_category_filter_id = self.category_filter_dict[self.selected_category]

        # Clear the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve stacks by selected category id
        self.populate_stacks(self.selected_category_filter_id)


"""
Description: A class for adding a stack
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class AddStackGui:

    def __init__(self, stack_window, list_stacks_gui, main_selected_category = None):
        self.list_stacks_gui = list_stacks_gui
        self.stack_window = stack_window
        self.main_selected_category = main_selected_category
        self.add_stack_window = tk.Toplevel(self.stack_window)
        self.add_stack_window.transient(self.stack_window)
        self.add_stack_window.title("Add Stack")
        self.add_stack_window.resizable(False, False)

        self.frame = tk.Frame(self.add_stack_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(620, 160)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Description field
        self.desc_label = ttk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=0, sticky="w")
        self.desc_entry = ttk.Entry(self.frame, width=61)
        self.desc_entry.grid(column=1, row=0, sticky="w", pady=(1, 2))

        # Category dropdown
        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(column=0, row=1, sticky="w")
        self.category_dict = self.populate_categories()
        self.category_combobox = ttk.Combobox(self.frame, values=list(self.category_dict.keys()), width=61)
        self.category_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))

        # Preselect the category
        if self.main_selected_category is None:
            self.category_combobox.current(0)
            self.selected_category_id = None
        else:
            # Prepopulate the category if a value was passed from the parent window
            self.category_combobox.set(self.main_selected_category)
            #print(self.category_dict)
            #print(self.main_selected_category)
            self.selected_category_id = self.category_dict[self.main_selected_category]

        # Bind the function to the Combobox selection event
        self.category_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Source field
        self.source_label = ttk.Label(self.frame, text="Source:")
        self.source_label.grid(column=0, row=2, sticky="w")
        self.source_entry = ttk.Entry(self.frame, width=61)
        self.source_entry.grid(column=1, row=2, sticky="w", pady=(1, 2))

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:")
        self.active_label.grid(column=0, row=3, sticky="w")
        self.active_var = tk.BooleanVar()
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=3, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=4, columnspan=2)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_stack)
        self.add_button.grid(column=0, row=0, pady=5)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.add_stack_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=5)

        self.add_stack_window.wait_visibility()
        self.add_stack_window.grab_set()

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_category(self):
        self.selected_category = self.category_combobox.get()
        self.selected_category_id = self.category_dict[self.selected_category]

    def add_stack(self):
        description = self.desc_entry.get()
        qcards_util = qu.QCardsUtil()
        category_id = qcards_util.get_selected_combobox_value(self.selected_category_id)
        source = self.source_entry.get()
        active = self.active_var.get()

        # Prepare Stack
        stack = sbl.Stack()
        stack.set_description(description)
        stack.set_category_id(category_id)
        stack.set_source(source)
        stack.set_active(active)

        # Store the new Stack in a database
        add_stack = sbl.AddStack()
        add_stack.run(stack)

        # Add the stack to the stack tree view
        #self.stack_window.tree.insert("", "end", text=desc, values=(active,))
        self.list_stacks_gui.populate_stacks(self.selected_category_id)

        # Show message
        #messagebox.showinfo("Stack added", f"{description} added to stacks.")

        # Close the form
        self.add_stack_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.add_stack_window.winfo_screenwidth(), self.add_stack_window.winfo_screenheight())
        self.add_stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

"""
Description: A class for updating a stack
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class UpdateStackGui:

    def __init__(self, stack_window, list_stacks_gui, stack, selected_category_filter_id):
        self.list_stacks_gui = list_stacks_gui
        self.stack_window = stack_window
        self.selected_category_filter_id = selected_category_filter_id
        self.update_stack_window = tk.Toplevel(self.stack_window)
        self.update_stack_window.transient(self.stack_window)
        self.update_stack_window.title("Update Stack")
        self.update_stack_window.resizable(False, False)

        self.frame = tk.Frame(self.update_stack_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(620, 180)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Populate the update window with the selected item's values
        self.id_var = tk.IntVar(value=stack.get_id())
        self.description_var = tk.StringVar(value=stack.get_description())
        self.source_var = tk.StringVar(value=stack.get_source())
        self.next_view_date = tk.StringVar(value=stack.get_next_view_date())
        self.review_stage_id = tk.IntVar(value=stack.get_review_stage_id())
        self.review_stage = tk.StringVar(value=stack.get_review_stage())
        self.active_var = tk.BooleanVar(value=stack.get_active())

        # Id field
        self.desc_label = ttk.Label(self.frame, text="ID:")
        self.desc_label.grid(column=0, row=0, sticky="w")
        self.desc_label = ttk.Label(self.frame, textvariable=self.id_var)
        self.desc_label.grid(column=1, row=0, sticky="w")

        # Description field
        self.desc_label = ttk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=1, sticky="w")
        self.desc_entry = ttk.Entry(self.frame, textvariable=self.description_var, width=61)
        self.desc_entry.grid(column=1, row=1, sticky="w", pady=(1, 1))

        # Category dropdown
        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(column=0, row=2, sticky="w")
        # Load the dictionary for the combobox
        self.category_dict = self.populate_categories()

        # Preselect the combobox with the appropriate value
        qcards_util = qu.QCardsUtil()
        self.selected_category = qcards_util.get_dictionary_key_from_value(self.category_dict, stack.get_category_id())
        self.selected_category = catc.CategoryConstants.SELECT_CATEGORY.value if self.selected_category is None else self.selected_category
        self.selected_category_id = stack.get_category_id()

        # The values are the keys of the dictionary of stacks, which contains the descriptions of the stacks
        self.category_combobox = ttk.Combobox(self.frame, textvariable=self.selected_category, values=list(self.category_dict.keys()), width=61)
        self.category_combobox.grid(column=1, row=2, sticky="w", pady=(1, 2))
        self.category_combobox.set(self.selected_category)

        # Bind the function to the Combobox selection event
        self.category_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Source field
        self.source_label = ttk.Label(self.frame, text="Source:")
        self.source_label.grid(column=0, row=3, sticky="w")
        self.source_entry = ttk.Entry(self.frame, textvariable=self.source_var, width=61)
        self.source_entry.grid(column=1, row=3, sticky="w", pady=(1, 2))

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:", anchor='w')
        self.active_label.grid(column=0, row=4, sticky="w")
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=4, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=5, columnspan=2)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_stack)
        self.save_button.grid(column=0, row=0, pady=5)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.update_stack_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=5)

        self.update_stack_window.wait_visibility()
        self.update_stack_window.grab_set()

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_category(self):
        # The selected_category_index will be the description of the stack, for example "Design Patterns"
        self.selected_category = self.category_combobox.get()
        self.selected_category_id = self.category_dict[self.selected_category]

    def save_stack(self):
        id = self.id_var.get()
        description = self.desc_entry.get()
        qcards_util = qu.QCardsUtil()
        category_id = qcards_util.get_selected_combobox_value(self.selected_category_id)
        source = self.source_entry.get()
        next_view_date = self.next_view_date.get()
        review_stage_id = self.review_stage_id.get()
        review_stage = self.review_stage.get()
        active = self.active_var.get()
        active_converted = qu.QCardsUtil().convert_boolean_to_tinyint(active)

        # Prepare Stack
        stack = sbl.Stack()
        stack.set_id(id)
        stack.set_description(description)
        stack.set_category_id(category_id)
        stack.set_source(source)
        stack.set_next_view_date(next_view_date)
        stack.set_active(active)

        # Store the new Stack in a database
        persist_stack = sbl.UpdateStack()
        persist_stack.run(stack);

        # Update the stack to the stack tree view
        selected_item = self.list_stacks_gui.tree.focus()
        self.list_stacks_gui.tree.item(selected_item, values=(id,
                                                              description,
                                                              "" if self.selected_category == catc.CategoryConstants.SELECT_CATEGORY.value else self.selected_category,
                                                              next_view_date,
                                                              None if review_stage_id == 0 else review_stage_id,
                                                              None if len(review_stage) == 0 else review_stage,
                                                              active))

        # Close the form
        self.update_stack_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.update_stack_window.winfo_screenwidth(), self.update_stack_window.winfo_screenheight())
        self.update_stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))
