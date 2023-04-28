import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import stack_bl as sbl
import qcards_gui_util as u
import qcards_util as qu
import category_bl as catbl

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
        self.stack_window.title("List Stacks")
        # Calculate the position of the center of the screen
        self.calculate_screen_position(1000, 500)

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
        self.category_filter_combobox = ttk.Combobox(self.category_filter_frame, values=list(self.category_filter_dict.keys()), width=80)
        self.category_filter_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.category_filter_combobox.current(0)
        self.selected_category_filter_id = None

        # Bind the function to the Combobox selection event
        self.category_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Define the columns
        columns = ('id', 'description', 'category', 'next_view_date', 'active')

        # Create a TreeView (Table)
        self.tree = ttk.Treeview(self.stack_window, columns=columns, show='headings')

        # Define the headings
        self.tree.heading('id', text="ID")
        self.tree.heading('description', text="Description")
        self.tree.heading('category', text="Category")
        self.tree.heading('next_view_date', text="Next View Date")
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
        add_stack_button.grid(row=0, column=0, padx=10, pady=10)
        update_stack_button = ttk.Button(self.button_frame, text="Update Stack", command=self.update_stack)
        update_stack_button.grid(row=0, column=1, padx=10, pady=10)
        refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh_table)
        refresh_button.grid(row=0, column=2, padx=10, pady=10)
        close_button = tk.Button(self.button_frame, text="Close", command=self.stack_window.destroy)
        close_button.grid(row=0, column=3, padx=10, pady=10)

        # Populate the grid with data
        self.populate_stacks()

        # Wait for the child window to be visible. wait_visibility() has to be called before grab_set
        self.stack_window.wait_visibility()
        # With grab_set(), give the stack_window focus, and prevent the main_window from being clickable
        self.stack_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.stack_window.winfo_screenwidth(), self.stack_window.winfo_screenheight())
        self.stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def populate_stacks(self, category_filter_id = None):
        all_stacks = []
        if category_filter_id == None or category_filter_id == -1:
            retrieve_all_stacks = sbl.RetrieveAllStacks()
            all_stacks = retrieve_all_stacks.run()
        else:
            # Retrieve stacks by category_filter_id
            retrieve_stacks_by_category_id = sbl.RetrieveActiveStacksByCategoryId()
            all_stacks = retrieve_stacks_by_category_id.run(category_filter_id)
        for stack in all_stacks:
            values = (stack[0], stack[1], stack[6], stack[5], stack[2])
            self.tree.insert('', tk.END, values=values)

    def add_stack(self):
        add_stack_gui = AddStackGui(self.stack_window, self)

    def update_stack(self):
        # Get values
        selected_item = self.tree.focus()

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
        update_stack_gui = UpdateStackGui(self.stack_window, self, stack)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_stacks()

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_category(self):
        # Get teh selected category
        selected_category = self.category_filter_combobox.get()
        self.selected_category_filter_id = self.category_filter_dict[selected_category]

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

    def __init__(self, stack_window, list_stacks_gui):
        self.list_stacks_gui = list_stacks_gui
        self.stack_window = stack_window
        self.add_stack_window = tk.Toplevel(self.stack_window)
        self.add_stack_window.transient(self.stack_window)
        self.add_stack_window.title("Add Stack")
        self.add_stack_window.resizable(False, False)

        self.frame = tk.Frame(self.add_stack_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(800, 150)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Description field
        self.desc_label = ttk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=0, sticky="w")
        self.desc_entry = ttk.Entry(self.frame, width=80)
        self.desc_entry.grid(column=1, row=0, sticky="w", pady=(1, 2))

        # Category dropdown
        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(column=0, row=1, sticky="w")
        self.category_dict = self.populate_categories()
        self.category_combobox = ttk.Combobox(self.frame, values=list(self.category_dict.keys()), width=80)
        self.category_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))
        self.category_combobox.current(0)
        self.selected_category_id = None

        # Bind the function to the Combobox selection event
        self.category_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Source field
        self.source_label = ttk.Label(self.frame, text="Source:")
        self.source_label.grid(column=0, row=2, sticky="w")
        self.source_entry = ttk.Entry(self.frame, width=80)
        self.source_entry.grid(column=1, row=2, sticky="w", pady=(1, 2))

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:")
        self.active_label.grid(column=0, row=3, sticky="w")
        self.active_var = tk.BooleanVar()
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=3, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=4)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_stack)
        self.add_button.grid(column=0, row=0)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.add_stack_window.destroy)
        self.cancel_button.grid(column=1, row=0)

        self.add_stack_window.wait_visibility()
        self.add_stack_window.grab_set()

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_category(self):
        selected_category = self.category_combobox.get()
        self.selected_category_id = self.category_dict[selected_category]

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
        self.list_stacks_gui.refresh_table()

        # Show message
        #messagebox.showinfo("Stack added", f"{description} added to stacks.")

        # Close the form
        self.add_stack_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.add_stack_window.winfo_screenwidth(), self.add_stack_window.winfo_screenheight())
        self.add_stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

"""
Description: A class for updating a stack
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class UpdateStackGui:

    def __init__(self, stack_window, list_stacks_gui, stack):
        self.list_stacks_gui = list_stacks_gui
        self.stack_window = stack_window
        self.update_stack_window = tk.Toplevel(self.stack_window)
        self.update_stack_window.transient(self.stack_window)
        self.update_stack_window.title("Update Stack")
        self.update_stack_window.resizable(False, False)

        self.frame = tk.Frame(self.update_stack_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(810, 170)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Populate the update window with the selected item's values
        self.id_var = tk.IntVar(value=stack.get_id())
        self.description_var = tk.StringVar(value=stack.get_description())
        self.source_var = tk.StringVar(value=stack.get_source())
        self.active_var = tk.BooleanVar(value=stack.get_active())

        # Id field
        self.desc_label = ttk.Label(self.frame, text="ID:")
        self.desc_label.grid(column=0, row=0, sticky="w")
        self.desc_label = ttk.Label(self.frame, textvariable=self.id_var)
        self.desc_label.grid(column=1, row=0, sticky="w")

        # Description field
        self.desc_label = ttk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=1, sticky="w")
        self.desc_entry = ttk.Entry(self.frame, textvariable=self.description_var, width=80)
        self.desc_entry.grid(column=1, row=1, sticky="w", pady=(1, 1))

        # Category dropdown
        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(column=0, row=2, sticky="w")
        # Load the dictionary for the combobox
        self.category_dict = self.populate_categories()
        # The values are the keys of the dictionary of stacks, which contains the descriptions of the stacks
        self.category_combobox = ttk.Combobox(self.frame, values=list(self.category_dict.keys()), width=80)
        self.category_combobox.grid(column=1, row=2, sticky="w", pady=(1, 2))

        # Preselect the value of the combobox
        if stack.get_category_id() == None:
            self.selected_category_index = 0
            self.selected_category_id = None
            self.selected_category = catbl.CategoryConstants.SELECT_CATEGORY.value
        else:
            qcards_util = qu.QCardsUtil()
            self.selected_category_index = qcards_util.convert_dict_value_to_index(self.category_dict, stack.get_category_id())
            self.selected_category_id = stack.get_category_id()
            self.selected_category = qcards_util.convert_index_to_dict_key(self.category_dict, self.selected_category_index)
        self.category_combobox.current(self.selected_category_index)

        # Bind the function to the Combobox selection event
        self.category_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Source field
        self.source_label = ttk.Label(self.frame, text="Source:")
        self.source_label.grid(column=0, row=3, sticky="w")
        self.source_entry = ttk.Entry(self.frame, textvariable=self.source_var, width=80)
        self.source_entry.grid(column=1, row=3, sticky="w", pady=(1, 2))

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:", anchor='w')
        self.active_label.grid(column=0, row=4, sticky="w")
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=4, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=5)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_stack)
        self.save_button.grid(column=0, row=0)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.update_stack_window.destroy)
        self.cancel_button.grid(column=1, row=0)

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
        active = self.active_var.get()
        active_converted = qu.QCardsUtil().convert_boolean_to_tinyint(active)

        # Prepare Stack
        stack = sbl.Stack()
        stack.set_id(id)
        stack.set_description(description)
        stack.set_category_id(category_id)
        stack.set_source(source)
        stack.set_active(active)

        # Store the new Stack in a database
        persist_stack = sbl.UpdateStack()
        persist_stack.run(stack);

        # Update the stack to the stack tree view
        selected_item = self.list_stacks_gui.tree.focus()
        self.list_stacks_gui.tree.item(selected_item, values=(id, description,
                                                                  "" if self.selected_category == catbl.CategoryConstants.SELECT_CATEGORY.value else self.selected_category,
                                                                    active))

        # Close the form
        self.update_stack_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.update_stack_window.winfo_screenwidth(), self.update_stack_window.winfo_screenheight())
        self.update_stack_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))
