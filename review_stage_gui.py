import tkinter as tk
from tkinter import ttk
import review_stage_bl as rsbl
import review_stage_constant as rsc

"""
Description: A class for managing the review stage for a stack
Author: Jaco Koekemoer
Date: 2023-04-28
"""
class ReviewStageGui:

    def __int__(self, main_window, stack):
        print("In review stage gui")
        self.category_window = tk.Toplevel(main_window)
        # With transient(), the category_window will always be displayed on top of the main window
        self.category_window.transient(main_window)
        self.category_window.title("Review Stage")
        # Calculate the position of the center of the screen
        self.calculate_screen_position(600, 500)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        # style.theme_use('clam')
        style.theme_use('alt')