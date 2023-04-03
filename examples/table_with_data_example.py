from tkinter import ttk
import tkinter as tk
import sqlite3

class DataViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Viewer")

        # Create a treeview widget to display the data
        self.tree = ttk.Treeview(self.master, columns=("ID", "Name", "Age"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Age")
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Load the data from the database and insert it into the treeview
        self.load_data()

        # Create an entry widget for searching the data
        self.search_entry = tk.Entry(self.master)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a button for searching the data
        self.search_button = tk.Button(self.master, text="Search", command=self.search_data)
        self.search_button.pack(side=tk.LEFT, padx=5, pady=5)

    def load_data(self):
        # Connect to the database and execute a SELECT query
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM mytable")
        rows = c.fetchall()

        # Insert the data into the treeview
        for row in rows:
            self.tree.insert("", tk.END, text=row[0], values=(row[0], row[1], row[2]))

        # Close the database connection
        conn.close()

    def search_data(self):
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())

        # Connect to the database and execute a SELECT query with a WHERE clause
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        search_term = self.search_entry.get()
        c.execute("SELECT * FROM mytable WHERE Name LIKE ?", ('%'+search_term+'%',))
        rows = c.fetchall()

        # Insert the search results into the treeview
        for row in rows:
            self.tree.insert("", tk.END, text=row[0], values=(row[0], row[1], row[2]))

        # Close the database connection
        conn.close()

# Create a main window and a button to open the data viewer
root = tk.Tk()
button = tk.Button(root, text="Open Data Viewer", command=lambda: DataViewer(tk.Toplevel(root)))
button.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
