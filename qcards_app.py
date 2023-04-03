import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmb
import category_gui as cg
import qcards_gui_util as u

class QCardsApp:

    def run(self):
        # Setup the main window
        self.main_window = tk.Tk()
        self.main_window.title("QCards")

        # Calculate the position of the center of the screen
        self.calculate_screen_position(1400, 650)

        # Creating a ttk style object
        style = ttk.Style(self.main_window)

        # Changing the theme to 'clam'
        #style.theme_use('clam')
        style.theme_use('alt')

        # Add a menubar
        menubar = tk.Menu(self.main_window)

        # Add the Category menu
        main_menu = tk.Menu(menubar, tearoff=0)
        main_menu.add_command(label="Categories", command=self.open_category_window)
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
        self.main_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1]))

    def open_category_window(self):
        list_categories_gui = cg.ListCategoriesGui(self.main_window)

app = QCardsApp()
app.run()
