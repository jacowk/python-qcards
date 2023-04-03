import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

class CategoryForm:
    def __init__(self, parent):
        self.parent = parent

        self.frame = tk.Frame(parent)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        self.desc_label = tk.Label(self.frame, text="Description:")
        self.desc_label.grid(column=0, row=0)
        self.desc_entry = tk.Entry(self.frame)
        self.desc_entry.grid(column=1, row=0)

        self.active_label = tk.Label(self.frame, text="Active:")
        self.active_label.grid(column=0, row=1)
        self.active_var = tk.BooleanVar()
        self.active_checkbutton = tk.Checkbutton(self.frame, variable=self.active_var)
        self.active_checkbutton.grid(column=1, row=1)

        self.add_button = tk.Button(self.frame, text="Add", command=self.add_category)
        self.add_button.grid(column=0, row=2)
        self.cancel_button = tk.Button(self.frame, text="Cancel", command=self.parent.destroy)
        self.cancel_button.grid(column=1, row=2)

    def add_category(self):
        desc = self.desc_entry.get()
        active = self.active_var.get()

        # Insert the category into the database
        conn = sqlite3.connect("categories.db")
        c = conn.cursor()
        c.execute("INSERT INTO categories (description, active) VALUES (?, ?)", (desc, active))
        conn.commit()
        conn.close()

        # Update the Treeview in the main window
        try:
            self.parent.parent.treeview.insert("", "end", text=desc, values=(active,))
        except AttributeError:
            # If the main window doesn't have a Treeview, just show a message box instead
            messagebox.showinfo("Category added", f"{desc} added to categories.")

        # Close the form
        self.parent.destroy()

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()

        # Set up the Treeview
        self.treeview = tk.ttk.Treeview(self.root, columns=("active",))
        self.treeview.heading("#0", text="Description")
        self.treeview.heading("active", text="Active")
        self.treeview.grid(column=0, row=0, padx=10, pady=10)

        # Set up the "Add category" button
        self.add_button = tk.Button(self.root, text="Add category", command=self.show_category_form)
        self.add_button.grid(column=0, row=1, padx=10, pady=10)

        # Populate the Treeview with categories from the database
        self.populate_treeview()

        self.root.mainloop()

    def show_category_form(self):
        category_form = tk.Toplevel(self.root)
        category_form.title("Add category")
        CategoryForm(category_form)

    def populate_treeview(self):
        conn = sqlite3.connect("categories.db")
        c = conn.cursor()
        c.execute("SELECT * FROM categories")
        rows = c.fetchall()
        for row in rows:
            desc, active = row
            self.treeview.insert("", "end", text=desc, values=(active,))
        conn.close()

if __name__ == "__main__":
    MainWindow()
