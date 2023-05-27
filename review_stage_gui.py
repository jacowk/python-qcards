import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import review_stage_bl as rsbl
import review_stage_constant as rsc
import qcards_date_util as qdu
import qcards_gui_util as u
import qcards_util as qu

"""
Description: A class for managing the review stage for a stack
Author: Jaco Koekemoer
Date: 2023-04-28
"""
class ReviewStageGui:

    def __init__(self, parent_window, stack, review_stage):
        self.parent_window = parent_window
        self.stack = stack
        self.review_stage = review_stage
        self.review_stage_window = tk.Toplevel(self.parent_window)
        # With transient(), the category_window will always be displayed on top of the main window
        self.review_stage_window.transient(self.parent_window)
        self.review_stage_window.title("Review Stage")
        self.review_stage_window.resizable(False, False)

        self.frame = tk.Frame(self.review_stage_window)
        self.frame.grid(column=0, row=0, padx=10, pady=1, sticky="w")

        # Calculate the position of the center of the screen
        self.calculate_screen_position(400, 200)

        # Creating a ttk style object
        style = ttk.Style()

        # Changing the theme to 'clam'
        # style.theme_use('clam')
        style.theme_use('alt')

        # Define a current date Frame above the table
        self.current_date_label = ttk.Label(self.frame, text="Today's Date:")
        self.current_date_label.grid(column=0, row=0, sticky="w")
        self.current_date = ttk.Label(self.frame, text=qdu.DateUtil.get_now_as_year_month_day())
        self.current_date.grid(column=1, row=0, sticky="w")

        # Stack ID
        self.stack_id_var = tk.IntVar(value=self.stack.get_id())
        self.stack_id_label = ttk.Label(self.frame, text="Stack ID:")
        self.stack_id_label.grid(column=0, row=1, sticky="w")
        self.stack_id_value = ttk.Label(self.frame, text=self.stack_id_var.get())
        self.stack_id_value.grid(column=1, row=1, sticky="w", pady=(1, 1))

        # Review Stage Cd
        self.review_stage_id_var = tk.IntVar(value=self.review_stage.get_id())
        self.review_stage_id_label = ttk.Label(self.frame, text="Review Stage ID:")
        self.review_stage_id_label.grid(column=0, row=2, sticky="w")
        self.review_stage_id_value = ttk.Label(self.frame, text=self.review_stage_id_var.get())
        self.review_stage_id_value.grid(column=1, row=2, sticky="w", pady=(1, 1))

        # Review Stage Combobox
        self.review_stage_label = ttk.Label(self.frame, text="Review Stage:")
        self.review_stage_label.grid(column=0, row=3, sticky="w")
        self.review_stage_lookup_dict = self.populate_review_stage_lookup_dict()
        qcards_util = qu.QCardsUtil()
        self.review_stage_lookup = qcards_util.get_dictionary_key_from_value(self.review_stage_lookup_dict, self.review_stage.get_review_stage_cd())
        self.review_stage_lookup = rsc.ReviewStageSelectValues.SELECT_REVIEW_STAGE.value if self.review_stage_lookup is None else self.review_stage_lookup
        self.review_stage_lookup_cd = self.review_stage.get_review_stage_cd()

        # The values are the keys of the dictionary of stacks, which contains the descriptions of the stacks
        self.review_stage_lookup_combobox = ttk.Combobox(self.frame, textvariable=self.review_stage_lookup,
                                                         values=list(self.review_stage_lookup_dict.keys()), width=30)
        self.review_stage_lookup_combobox.grid(column=1, row=3, sticky="w", pady=(1, 2))
        self.review_stage_lookup_combobox.set(self.review_stage_lookup)

        # Bind the function to the Combobox selection event
        self.review_stage_lookup_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_review_stage())

        # Create another frame for the review specific fields
        self.review_stage_frame = tk.Frame(self.review_stage_window)
        self.review_stage_frame.grid(column=0, row=1, padx=10, pady=1, sticky="w")

        # =======================================================
        # Every 2nd Day
        # =======================================================
        self.every_2nd_day_frame = tk.Frame(self.review_stage_frame)
        #self.every_2nd_day_frame.grid(column=0, row=4, sticky="w", pady=(1, 1))

        # Odd or even combobox
        self.odd_even_label = ttk.Label(self.every_2nd_day_frame, text="Review on Odd or Even days?")
        self.odd_even_label.grid(column=0, row=0, sticky="w")

        self.odd_even_lookup_dict = self.populate_odd_even_lookup_dict()
        qcards_util = qu.QCardsUtil()
        self.odd_even_lookup = qcards_util.get_dictionary_key_from_value(self.odd_even_lookup_dict, self.review_stage.get_odd_even_cd())
        self.odd_even_lookup = rsc.ReviewStageSelectValues.SELECT_ODD_OR_EVEN.value if self.odd_even_lookup is None else self.odd_even_lookup
        self.odd_even_lookup_cd = self.review_stage.get_odd_even_cd()

        # The values are the keys of the dictionary of stacks, which contains the descriptions of the stacks
        self.odd_even_lookup_combobox = ttk.Combobox(self.every_2nd_day_frame, textvariable=self.odd_even_lookup,
                                                         values=list(self.odd_even_lookup_dict.keys()), width=20)
        self.odd_even_lookup_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.odd_even_lookup_combobox.set(self.odd_even_lookup)

        # Bind the function to the Combobox selection event
        self.odd_even_lookup_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_odd_even())


        # =======================================================
        # Weekly
        # =======================================================
        self.weekly_frame = tk.Frame(self.review_stage_frame)
        #self.weekly_frame.grid(column=0, row=5, sticky="w", pady=(1, 1))

        # Weekday
        self.weekday_label = ttk.Label(self.weekly_frame, text="Review on which weekday?")
        self.weekday_label.grid(column=0, row=0, sticky="w")

        # Weekday combobox
        self.weekday_lookup_dict = self.populate_weekday_lookup_dict()
        qcards_util = qu.QCardsUtil()
        self.weekday_lookup = qcards_util.get_dictionary_key_from_value(self.weekday_lookup_dict,
                                                                         self.review_stage.get_weekday_cd())
        self.weekday_lookup = rsc.ReviewStageSelectValues.SELECT_WEEKDAY.value if self.weekday_lookup is None else self.weekday_lookup
        self.weekday_lookup_cd = self.review_stage.get_weekday_cd()

        # The values are the keys of the dictionary of stacks, which contains the descriptions of the stacks
        self.weekday_lookup_combobox = ttk.Combobox(self.weekly_frame, textvariable=self.weekday_lookup,
                                                     values=list(self.weekday_lookup_dict.keys()), width=20)
        self.weekday_lookup_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.weekday_lookup_combobox.set(self.weekday_lookup)

        # Bind the function to the Combobox selection event
        self.weekday_lookup_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_weekday())

        # Week count
        self.week_count_label = ttk.Label(self.weekly_frame, text="Review every ? week(s)")
        self.week_count_label.grid(column=0, row=1, sticky="w")

        # Weekday count combobox
        self.week_count = self.review_stage.get_week_count()
        self.week_count_combobox = ttk.Combobox(self.weekly_frame, textvariable=self.week_count,
                                                    values=[1,2,3], width=5)
        self.week_count_combobox.grid(column=1, row=1, sticky="w", pady=1)
        self.week_count_combobox.set(self.week_count)

        # Bind the function to the Combobox selection event
        self.week_count_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_week_count())

        # =======================================================
        # Monthly
        # =======================================================
        self.monthly_frame = tk.Frame(self.review_stage_frame)
        #self.monthly_frame.grid(column=0, row=6, sticky="w", pady=(1, 1))

        # Calendar day
        self.calendar_day_label = ttk.Label(self.monthly_frame, text="Calendar Day:")
        self.calendar_day_label.grid(column=0, row=0, sticky="w")

        # Calendar day combobox
        self.calendar_day = self.review_stage.get_calendar_day()
        calendar_day_list = list(range(1, 32))
        self.calendar_day_combobox = ttk.Combobox(self.monthly_frame, textvariable=self.calendar_day,
                                                 values=calendar_day_list, width=5)
        self.calendar_day_combobox.grid(column=1, row=0, sticky="w", pady=(1, 2))
        self.calendar_day_combobox.set(self.calendar_day)

        # Bind the function to the Combobox selection event
        self.calendar_day_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_calendar_day())

        # Month count
        self.month_count_label = ttk.Label(self.monthly_frame, text="Review every ? month(s)")
        self.month_count_label.grid(column=0, row=1, sticky="w")

        # Month count combobox
        self.month_count = self.review_stage.get_month_count()
        month_count_list = list(range(1, 6))
        self.month_count_combobox = ttk.Combobox(self.monthly_frame, textvariable=self.month_count,
                                                values=month_count_list, width=5)
        self.month_count_combobox.grid(column=1, row=1, sticky="w", pady=(1, 2))
        self.month_count_combobox.set(self.month_count)

        # Bind the function to the Combobox selection event
        self.month_count_combobox.bind("<<ComboboxSelected>>", lambda event: self.get_selected_month_count())

        #=======================================================
        # Buttons
        # =======================================================

        # Button frame
        self.button_frame = tk.Frame(self.review_stage_window)
        self.button_frame.grid(column=0, row=2, pady=1)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_review_stage)
        self.save_button.grid(column=0, row=0)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.review_stage_window.destroy)
        self.cancel_button.grid(column=1, row=0)

        self.display_review_stage_frame()

        # Give the window focus
        self.review_stage_window.wait_visibility()
        self.review_stage_window.grab_set()

    def calculate_screen_position(self, x, y):
        gui_util = u.QCardsGUIUtil()
        screen_coordinates = gui_util.calculate_window_center(x, y, self.review_stage_window.winfo_screenwidth(), self.review_stage_window.winfo_screenheight())
        self.review_stage_window.geometry("{}x{}+{}+{}".format(x, y, screen_coordinates[0], screen_coordinates[1] - 50))

    def populate_review_stage_lookup_dict(self):
        review_stage_lookup = rsbl.ReviewStageLookupDict()
        return review_stage_lookup.run()

    def get_selected_review_stage(self):
        selected_review_stage = self.review_stage_lookup_combobox.get()
        self.review_stage_lookup_cd = self.review_stage_lookup_dict[selected_review_stage]
        self.display_review_stage_frame()

    def populate_odd_even_lookup_dict(self):
        odd_even_lookup = rsbl.OddEvenLookupDict()
        return odd_even_lookup.run()

    def get_selected_odd_even(self):
        selected_odd_even = self.odd_even_lookup_combobox.get()
        self.odd_even_lookup_cd = self.odd_even_lookup_dict[selected_odd_even]

    def populate_weekday_lookup_dict(self):
        weekday_lookup = rsbl.WeekdayLookupDict()
        return weekday_lookup.run()

    def get_selected_weekday(self):
        selected_weekday = self.weekday_lookup_combobox.get()
        self.weekday_lookup_cd = self.weekday_lookup_dict[selected_weekday]

    def get_selected_week_count(self):
        self.week_count = self.week_count_combobox.get()

    def get_selected_calendar_day(self):
        self.calendar_day = self.calendar_day_combobox.get()

    def get_selected_month_count(self):
        self.month_count = self.month_count_combobox.get()

    def display_review_stage_frame(self):
        if self.review_stage_lookup_cd == rsc.ReviewStage.DAILY.value:
            self.every_2nd_day_frame.grid_remove()
            self.weekly_frame.grid_remove()
            self.monthly_frame.grid_remove()
        elif self.review_stage_lookup_cd == rsc.ReviewStage.EVERY_2ND_DAY.value:
            self.every_2nd_day_frame.grid(column=0, row=0, sticky="w", pady=(1, 1))
            self.weekly_frame.grid_remove()
            self.monthly_frame.grid_remove()
        elif self.review_stage_lookup_cd == rsc.ReviewStage.WEEKLY.value:
            self.every_2nd_day_frame.grid_remove()
            self.weekly_frame.grid(column=0, row=0, sticky="w", pady=(1, 1))
            self.monthly_frame.grid_remove()
        elif self.review_stage_lookup_cd == rsc.ReviewStage.MONTHLY.value:
            self.every_2nd_day_frame.grid_remove()
            self.weekly_frame.grid_remove()
            self.monthly_frame.grid(column=0, row=0, sticky="w", pady=(1, 1))
        else:
            self.every_2nd_day_frame.grid_remove()
            self.weekly_frame.grid_remove()
            self.monthly_frame.grid_remove()

    def save_review_stage(self):
        # Prepare parameters
        self.review_stage.set_review_stage_cd(self.review_stage_lookup_cd)
        self.review_stage.set_odd_even_cd(self.odd_even_lookup_cd)
        self.review_stage.set_weekday_cd(self.weekday_lookup_cd)
        self.review_stage.set_week_count(self.week_count)
        self.review_stage.set_calendar_day(self.calendar_day)
        self.review_stage.set_month_count(self.month_count)

        # Update review stage
        update_review_stage = rsbl.UpdateReviewStage()
        update_review_stage.run(self.review_stage)

        # Display a message
        messagebox.showinfo("Information", "Review stage updated. Remember to click on Calc Next View Date, to calculate " \
                                           "a next view date based on the new review stage")

        # Close the form
        self.review_stage_window.destroy()

