import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import category_dao as mc
import qcards_gui_util as u
import qcards_util as qu

"""
Description: A class for listing categories
Author: Jaco Koekemoer
Date: 30 March 2023
"""
class ListCategoriesGui:

    def __init__(self, main_window):
        self.category_window = tk.Toplevel(main_window)
        self.category_window.title("List Categories")
        # Calculate the position of the center of the screen
        self.calculate_screen_position(600, 500)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Define the columns
        columns = ('id', 'description', 'active')

        # Create a TreeView (Table)
        self.tree = ttk.Treeview(self.category_window, columns=columns, show='headings')

        # Define the headings
        self.tree.heading('id', text="ID")
        self.tree.heading('description', text="Description")
        self.tree.heading('active', text="Active")

        # Change column widths
        self.tree.column("id", anchor=tk.CENTER, stretch=tk.NO, width=100)
        self.tree.column("active", anchor=tk.CENTER, stretch=tk.NO, width=100)

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
        add_category_button.grid(row=0, column=0, padx=10, pady=10)
        update_category_button = ttk.Button(self.button_frame, text="Update Category", command=self.update_category)
        update_category_button.grid(row=0, column=1, padx=10, pady=10)
        refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh_table)
        refresh_button.grid(row=0, column=2, padx=10, pady=10)

        # Populate the grid with data
        self.populate_categories()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.category_window.winfo_screenwidth(), self.category_window.winfo_screenheight())
        self.category_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def populate_categories(self):
        retrieve_all_categories = mc.RetrieveAllCategories()
        all_categories = retrieve_all_categories.run()
        for category in all_categories:
            self.tree.insert('', tk.END, values=category)

    def add_category(self):
        add_category_gui = AddCategoryGui(self.category_window, self)

    def update_category(self):
        # Get values
        selected_item = self.tree.focus()

        # Current_item is a dictionary
        current_item = self.tree.item(selected_item)

        # Get the values index from the dictionary, which contains a list
        values = current_item['values']

        # Each item in the list corresponds with the columns in the TreeView
        id = values[0]
        description = values[1]
        active = values[2]

        # Run the update GUI
        update_category_gui = UpdateCategoryGui(self.category_window, self, id, description, active)

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
        self.add_category_window.title("Add Category")

        self.frame = tk.Frame(self.add_category_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(350, 120)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Description field
        self.desc_label = ttk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=0, sticky="w")
        self.desc_entry = ttk.Entry(self.frame)
        self.desc_entry.grid(column=1, row=0)

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:")
        self.active_label.grid(column=0, row=1, sticky="w")
        self.active_var = tk.BooleanVar()
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=1, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=3)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_category)
        self.add_button.grid(column=0, row=0)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.add_category_window.destroy)
        self.cancel_button.grid(column=1, row=0)

    def add_category(self):
        description = self.desc_entry.get()
        active = self.active_var.get()

        # Store the new Category in a database
        persist_category = mc.AddCategory()
        persist_category.run(description, active);

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
        self.add_category_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

"""
Description: A class for updating a category
Author: Jaco Koekemoer
Date: 31 March 2023
"""
class UpdateCategoryGui:

    def __init__(self, category_window, list_categories_gui, id, description, active):
        self.list_categories_gui = list_categories_gui
        self.category_window = category_window
        self.update_category_window = tk.Toplevel(self.category_window)
        self.update_category_window.title("Update Category")

        self.frame = tk.Frame(self.update_category_window)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Calculate the position of the center of the screen
        self.calculate_screen_position(350, 120)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        style.theme_use('clam')
        #style.theme_use('alt')

        # Populate the update window with the selected item's values
        self.id_var = tk.IntVar(value=id)
        self.description_var = tk.StringVar(value=description)
        self.active_var = tk.BooleanVar(value=active)

        # Id field
        self.desc_label = ttk.Label(self.frame, text="ID:")
        self.desc_label.grid(column=0, row=0, sticky="w")
        self.desc_label = ttk.Label(self.frame, textvariable=self.id_var)
        self.desc_label.grid(column=1, row=0, sticky="w")

        # Description field
        self.desc_label = ttk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=1, sticky="w")
        self.desc_entry = ttk.Entry(self.frame, textvariable=self.description_var)
        self.desc_entry.grid(column=1, row=1)

        # Active checkbox
        self.active_label = tk.Label(self.frame, text="Active:", anchor='w')
        self.active_label.grid(column=0, row=2, sticky="w")
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=2, sticky="w")

        # Button frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(column=0, row=3)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_category)
        self.save_button.grid(column=0, row=0)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.update_category_window.destroy)
        self.cancel_button.grid(column=1, row=0)

    def save_category(self):
        id = self.id_var.get()
        description = self.desc_entry.get()
        active = self.active_var.get()
        active_converted = qu.QCardsUtil().convert_boolean_to_tinyint(active)

        # Store the new Category in a database
        persist_category = mc.UpdateCategory()
        persist_category.run(id, description, active);

        # Update the category to the category tree view
        selected_item = self.list_categories_gui.tree.focus()
        self.list_categories_gui.tree.item(selected_item, values=(id, description, active))

        # Close the form
        self.update_category_window.destroy()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.update_category_window.winfo_screenwidth(), self.update_category_window.winfo_screenheight())
        self.update_category_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))
