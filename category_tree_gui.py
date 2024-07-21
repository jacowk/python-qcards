import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import category_bl as catbl
import json

"""
Description: A user interface for displaying categories as a tree
Author: Jaco Koekemoer
Date: 2023-05-05
"""
class CategoryTreeGui:

    def __init__(self, main_window):
        self.category_window = tk.Toplevel(main_window)
        # With transient(), the category_window will always be displayed on top of the main window
        self.category_window.transient(main_window)
        self.category_window.title("Category Tree")
        # Retrieve the category data as a tree
        retrieve_category_tree = catbl.RetrieveCategoryTree()
        category_tree_data = retrieve_category_tree.run()

        self.treeview = ttk.Treeview(self.category_window, selectmode='browse')
        self.treeview.config(height=30)
        self.treeview.pack(expand=YES, fill=BOTH)
        self.treeview.heading("#0", text="Categories")
        # By setting minwidth > width, and stretch=True, horizontal scrollbar works
        self.treeview.column("#0", minwidth=300, width=300, stretch=True)
        # Automatically expand all nodes on open
        self.treeview.bind('<<TreeviewOpen>>', self.handleOpenEvent)

        # Constructing horizontal scrollbar with treeview
        self.horizontal_scrollbar = ttk.Scrollbar(self.category_window,
                                                  orient="horizontal",
                                                  command=self.treeview.xview)
        # Configuring treeview
        self.treeview.configure(xscrollcommand=self.horizontal_scrollbar.set)

        # ----------------------------------------------------------
        # Constructing vertical scrollbar with treeview
        self.vertical_scrollbar = ttk.Scrollbar(self.category_window,
                                                orient="vertical",
                                                command=self.treeview.yview)

        # Configuring treeview
        self.treeview.configure(yscrollcommand=self.vertical_scrollbar.set)

        # ----------------------------------------------------------

        for node in category_tree_data:
            name = "{}".format(node['name'])
            self.treeview.insert('', 'end', name, text=name)
            first_children = node['children']
            for child in first_children:
                self.add_item(name, child)

        # Place on grid
        self.treeview.grid(row=0, column=0)
        self.vertical_scrollbar.grid(row=0, column=2, rowspan=2, sticky=NS)
        self.horizontal_scrollbar.grid(row=1, column=0, columnspan=2, sticky=EW)
        # self.genealogy_selection_combo.grid(row=1, column=0)

    def add_item(self, parent_name, item):
        name = item['name']
        name = "{}".format(name)
        self.treeview.insert(parent_name, 'end', name, text=name)

        try:
            children = item['children']
            for child in children:
                self.add_item(name, child)
        except:
            print("No children for {}".format(name))

    def open_children(self, parent):
        self.treeview.item(parent, open=True)
        for child in self.treeview.get_children(parent):
            self.open_children(child)

    def handleOpenEvent(self, event):
        self.open_children(self.treeview.focus())
