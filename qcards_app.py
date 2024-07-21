import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import category_tree_gui as ctg
import category_gui as catg
import stack_gui as sg
import card_gui as cg
import review_stack_gui as rg
import qcards_gui_util as u
import card_csv_import_gui as ci

"""
Description: The main class for this QCards app
Author: Jaco Koekemoer
Date: 2023-03-30

Run Squirrel: sudo /usr/local/squirrel-sql-4.7.1/squirrel-sql.sh
"""
class QCardsApp:

    def run(self):
        # Setup the main window
        self.main_window = tk.Tk()
        self.main_window.title("QCards")

        # Calculate the position of the center of the screen
        self.calculate_screen_position(1024, 600)

        # Image frame
        self.image_frame = tk.Frame(self.main_window, width=1200, height=500)
        self.image_frame.grid(row=0, column=0, columnspan=2)
        img = ImageTk.PhotoImage(Image.open("images/pinetree.jpg"))
        self.image_label = tk.Label(self.image_frame, image=img)
        self.image_label.grid(row=0, column=0, columnspan=2)

        # Creating a ttk style object
        style = ttk.Style(self.main_window)

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Add a menubar
        menubar = tk.Menu(self.main_window)

        # Add the Category menu
        main_menu = tk.Menu(menubar, tearoff=0)

        main_menu.add_command(label="Category Tree", command=self.open_category_tree_window)
        main_menu.add_separator()
        main_menu.add_command(label="Categories", command=self.open_category_window)
        main_menu.add_command(label="Stacks", command=self.open_stack_window)
        main_menu.add_command(label="Cards", command=self.open_card_window)
        main_menu.add_separator()
        main_menu.add_command(label="Review", command=self.open_review_window)
        main_menu.add_separator()
        main_menu.add_command(label="Import Cards", command=self.open_import_cards_window)
        main_menu.add_separator()
        main_menu.add_command(label="Exit", command=self.main_window.quit)

        menubar.add_cascade(label="Menu", menu=main_menu)

        # Add menu to the main window
        self.main_window.config(menu=menubar)

        # Adding a frame
        #frame = tk.Frame(main_window)
        #frame.pack()

        self.main_window.mainloop()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight())
        self.main_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

    def open_category_tree_window(self):
        category_tree_gui = ctg.CategoryTreeGui(self.main_window)

    def open_category_window(self):
        list_categories_gui = catg.ListCategoriesGui(self.main_window)

    def open_stack_window(self):
        list_stacks_gui = sg.ListStacksGui(self.main_window)

    def open_card_window(self):
        list_cards_gui = cg.ListCardsGui(self.main_window)

    def open_review_window(self):
        review_gui = rg.ReviewGui(self.main_window)

    def open_import_cards_window(self):
        card_import = ci.CardCSVImportGui(self.main_window)

app = QCardsApp()
app.run()
