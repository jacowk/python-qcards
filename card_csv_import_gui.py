import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as messagebox
import qcards_gui_util as u
import category_bl as catbl
import stack_bl as sbl
import card_bl as cbl

"""
Description: A GUI that can be used to import a stack of cards from a CSV file
"""
class CardCSVImportGui:

    def __init__(self, main_window):
        self.import_cards_window = tk.Toplevel(main_window)
        # With transient(), the card_window will always be displayed on top of the main window
        self.import_cards_window.transient(main_window)
        self.import_cards_window.title("Import Cards")
        # Calculate the position of the center of the screen
        self.calculate_screen_position(720, 140)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        # style.theme_use('clam')
        style.theme_use('alt')

        # Define a Category Frame above the table
        self.import_file_frame = tk.Frame(self.import_cards_window)
        self.import_file_frame.grid(row=0, column=0, columnspan=2)

        # Add a category filter dropdown
        self.category_filter_label = ttk.Label(self.import_file_frame, text="Select category:")
        self.category_filter_label.grid(column=0, row=0, sticky="w")
        self.category_filter_dict = self.populate_categories()
        self.category_filter_combobox = ttk.Combobox(self.import_file_frame,
                                                     values=list(self.category_filter_dict.keys()), width=61)
        self.category_filter_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.category_filter_combobox.current(0)
        self.selected_category_filter_id = None

        # Bind the function to the Combobox selection event
        self.category_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_category())

        # Add a stack filter dropdown
        self.stack_filter_label = ttk.Label(self.import_file_frame, text="Select stack:")
        self.stack_filter_label.grid(column=0, row=1, sticky="w")
        self.stack_filter_combobox = ttk.Combobox(self.import_file_frame, width=61)
        self.stack_filter_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))
        self.selected_stack_filter_id = None

        # Bind the function to the Combobox selection event
        self.stack_filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_stack())

        # Select a file
        self.filename_var = tk.StringVar("")
        self.select_file_label = ttk.Label(self.import_file_frame, text="Select file:")
        self.select_file_label.grid(column=0, row=2, sticky="w")
        self.select_file_entry = ttk.Entry(self.import_file_frame, textvariable=self.filename_var, width=61)
        self.select_file_entry.grid(column=1, row=2, sticky="w", pady=(1, 2))
        self.select_file_button = tk.Button(self.import_file_frame, text="Select File", command=self.select_file)
        self.select_file_button.grid(column=2, row=2)

        # Button frame
        self.button_frame = tk.Frame(self.import_file_frame)
        self.button_frame.grid(column=0, row=3, columnspan=2)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Import File", command=self.import_file)
        self.add_button.grid(column=0, row=0, pady=(1, 2))
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.import_cards_window.destroy)
        self.cancel_button.grid(column=1, row=0, pady=(1, 2))

        self.import_cards_window.wait_visibility()
        self.import_cards_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.import_cards_window.winfo_screenwidth(), self.import_cards_window.winfo_screenheight())
        self.import_cards_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

    def populate_categories(self):
        retrieve_all_categories = catbl.RetrieveAllCategoriesDict()
        return retrieve_all_categories.run()

    def get_selected_category(self):
        # Get teh selected category
        selected_category = self.category_filter_combobox.get()
        self.selected_category_filter_id = self.category_filter_dict[selected_category]

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
        selected_stack = self.stack_filter_combobox.get()
        self.selected_stack_filter_id = self.stack_filter_dict[selected_stack]

    def select_file(self):
        self.filename = fd.askopenfilename()
        self.filename_var.set(self.filename)

    def import_file(self):
        # Perform validations
        if self.selected_stack_filter_id is None or self.selected_stack_filter_id < 1:
            messagebox.showerror("Error", "A stack must be selected")
            return

        if self.filename_var is None or len(self.filename_var.get()) == 0:
            messagebox.showerror("Error", "A file must be selected")
            return

        print("Importing from {:s} for stack {:d}".format(self.filename_var.get(), self.selected_stack_filter_id))

        # Import the file
        import_card = cbl.ImportCards()
        import_card.run(self.selected_stack_filter_id, self.filename_var.get())

        messagebox.showinfo("Import", "File import done")
        self.import_cards_window.destroy()
