import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import category_bl as catbl
import qcards_gui_util as u
import qcards_util as qu
import category_constant as catc

"""
Description: A class for listing categories
Author: Jaco Koekemoer
Date: 2023-03-30
"""
class ListCategoriesGui:

    def __init__(self, main_window):
        self.category_window = tk.Toplevel(main_window)
        # With transient(), the category_window will always be displayed on top of the main window
        self.category_window.transient(main_window)
        # Calculate the position of the center of the screen
        self.calculate_screen_position(600, 520)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Define the columns
        columns = ('id', 'description', 'parent', 'active')

        # Create a TreeView (Table)
        self.tree = ttk.Treeview(self.category_window, columns=columns, show='headings')

        # Define the headings
        self.tree.heading('id', text="ID")
        self.tree.heading('description', text="Description")
        self.tree.heading('parent', text="Parent")
        self.tree.heading('active', text="Active")

        # Change column widths
        self.tree.column("id", anchor=tk.CENTER, stretch=tk.NO, width=90)
        self.tree.column("active", anchor=tk.CENTER, stretch=tk.NO, width=90)

        # Place the TreeView on the grid
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Define a scrollbar
        scrollbar = ttk.Scrollbar(self.category_window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Configure the row and column weights
        self.category_window.rowconfigure(0, weight=1)
        self.category_window.columnconfigure(0, weight=1)

        # Define a button Frame below the table
        self.button_frame = tk.Frame(self.category_window)
        self.button_frame.grid(row=1, column=0, columnspan=2)

        # Add buttons
        add_category_button = ttk.Button(self.button_frame, text="Add Category", command=self.add_category)
        add_category_button.grid(row=0, column=0, pady=5)
        update_category_button = ttk.Button(self.button_frame, text="Update Category", command=self.update_category)
        update_category_button.grid(row=0, column=1, pady=5)
        refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh_table)
        refresh_button.grid(row=0, column=2, pady=5)
        close_button = tk.Button(self.button_frame, text="Close", command=self.category_window.destroy)
        close_button.grid(row=0, column=3, pady=5)

        # Populate the grid with data
        self.populate_categories()

        # Wait for the child window to be visible. wait_visibility() has to be called before grab_set
        self.category_window.wait_visibility()
        # With grab_set(), give the category_window focus, and prevent the main_window from being clickable
        self.category_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.category_window.winfo_screenwidth(), self.category_window.winfo_screenheight())
        self.category_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategories()
        all_categories = retrieve_all_categories.run()
        for category in all_categories:
            self.tree.insert('', tk.END, values=category)

        self.category_window.title("List Categories ({}) categories".format(len(all_categories)))

    def add_category(self):
        add_category_gui = AddCategoryGui(self.category_window, self)

    def update_category(self):
        # Get values
        selected_item = self.tree.focus()

        # If no selection was made, display an error message
        if len(selected_item) == 0:
            messagebox.showerror("Error", "Please select a category to update")
            return

        # Current_item is a dictionary
        current_item = self.tree.item(selected_item)

        # Get the values index from the dictionary, which contains a list
        values = current_item['values']

        # Each item in the list corresponds with the columns in the TreeView
        id = values[0]

        # Retrieve the category from the database
        retrieve_category = catbl.RetrieveCategoryById()
        category = retrieve_category.run(id)

        # Run the update GUI
        update_category_gui = UpdateCategoryGui(self.category_window, self, category)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_categories()

"""
Description: A class for adding a category
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class AddCategoryGui:

    def __init__(self, category_window, list_categories_gui):
        self.list_categories_gui = list_categories_gui
        self.category_window = category_window
        self.add_category_window = tk.Toplevel(self.category_window)
        self.add_category_window.transient(self.category_window)
        self.add_category_window.title("Add Category")
        self.add_category_window.resizable(False, False)

        self.frame = tk.Frame(self.add_category_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(620, 130)

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

        # Parent dropdown
        self.parent_label = ttk.Label(self.frame, text="Parent:")
        self.parent_label.grid(column=0, row=1, sticky="w")
        self.parent_category_dict = self.populate_parent_categories()
        self.parent_combobox = ttk.Combobox(self.frame, values=list(self.parent_category_dict.keys()), width=61)
        self.parent_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))
        self.parent_combobox.current(0)
        self.selected_parent_id = None

        # Bind the function to the Combobox selection event
        self.parent_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_parent())

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:")
        self.active_label.grid(column=0, row=2, sticky="w")
        self.active_var = tk.BooleanVar()
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=2, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=3, columnspan=2)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_category)
        self.add_button.grid(column=0, row=0, pady=5)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.add_category_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=5)

        self.add_category_window.wait_visibility()
        self.add_category_window.grab_set()

    def populate_parent_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_parent(self):
        selected_parent = self.parent_combobox.get()
        self.selected_parent_id = self.parent_category_dict[selected_parent]

    def add_category(self):
        description = self.desc_entry.get()
        qcards_util = qu.QCardsUtil()
        parent_id = qcards_util.get_selected_combobox_value(self.selected_parent_id)
        active = self.active_var.get()

        # Prepare Category
        category = catbl.Category()
        category.set_description(description)
        category.set_parent_id(parent_id)
        category.set_active(active)

        # Store the new Category in a database
        add_category = catbl.AddCategory()
        add_category.run(category)

        # Add the category to the category tree view
        #self.category_window.tree.insert("", "end", text=desc, values=(active,))
        self.list_categories_gui.refresh_table()

        # Show message
        #messagebox.showinfo("Category added", f"{description} added to categories.")

        # Close the form
        self.add_category_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.add_category_window.winfo_screenwidth(), self.add_category_window.winfo_screenheight())
        self.add_category_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

"""
Description: A class for updating a category
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class UpdateCategoryGui:

    def __init__(self, category_window, list_categories_gui, category):
        self.list_categories_gui = list_categories_gui
        self.category_window = category_window
        self.update_category_window = tk.Toplevel(self.category_window)
        self.update_category_window.transient(self.category_window)
        self.update_category_window.title("Update Category")
        self.update_category_window.resizable(False, False)

        self.frame = tk.Frame(self.update_category_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(628, 150)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Populate the update window with the selected item's values
        self.id_var = tk.IntVar(value=category.get_id())
        self.description_var = tk.StringVar(value=category.get_description())
        self.active_var = tk.BooleanVar(value=category.get_active())

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

        # Parent dropdown
        self.parent_label = ttk.Label(self.frame, text="Parent:")
        self.parent_label.grid(column=0, row=2, sticky="w")
        # Load the dictionary for the combobox
        self.parent_category_dict = self.populate_parent_categories()

        # Preselect the combobox with the appropriate value
        qcards_util = qu.QCardsUtil()
        self.selected_parent = qcards_util.get_dictionary_key_from_value(self.parent_category_dict, category.get_parent_id())
        self.selected_parent = catc.CategoryConstants.SELECT_PARENT.value if self.selected_parent is None else self.selected_parent
        self.selected_parent_id = category.get_parent_id()

        # The values are the keys of the dictionary of categories, which contains the descriptions of the categories
        self.parent_combobox = ttk.Combobox(self.frame, textvariable=self.selected_parent, values=list(self.parent_category_dict.keys()), width=61)
        self.parent_combobox.grid(column=1, row=2, sticky="w", pady=(1, 2))
        self.parent_combobox.set(self.selected_parent)

        # Bind the function to the Combobox selection event
        self.parent_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_parent())

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:", anchor='w')
        self.active_label.grid(column=0, row=3, sticky="w")
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=3, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=4, columnspan=2)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_category)
        self.save_button.grid(column=0, row=0, pady=5)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.update_category_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=5)

        self.update_category_window.wait_visibility()
        self.update_category_window.grab_set()

    def populate_parent_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    # Define a function to get the selected value from the dictionary
    def get_selected_parent(self):
        # The selected_parent_index will be the description of the category, for example "Design Patterns"
        self.selected_parent = self.parent_combobox.get()
        self.selected_parent_id = self.parent_category_dict[self.selected_parent]

    def save_category(self):
        id = self.id_var.get()
        description = self.desc_entry.get()
        qcards_util = qu.QCardsUtil()
        parent_id = qcards_util.get_selected_combobox_value(self.selected_parent_id)
        active = self.active_var.get()
        active_converted = qu.QCardsUtil().convert_boolean_to_tinyint(active)

        # Prepare Category
        category = catbl.Category()
        category.set_id(id)
        category.set_description(description)
        category.set_parent_id(parent_id)
        category.set_active(active)

        # Store the new Category in a database
        persist_category = catbl.UpdateCategory()
        persist_category.run(category);

        # Update the category to the category tree view
        selected_item = self.list_categories_gui.tree.focus()
        self.list_categories_gui.tree.item(selected_item, values=(id, description,
                                                                  "" if self.selected_parent == catc.CategoryConstants.SELECT_PARENT.value else self.selected_parent,
                                                                    active))

        # Close the form
        self.update_category_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.update_category_window.winfo_screenwidth(), self.update_category_window.winfo_screenheight())
        self.update_category_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))
