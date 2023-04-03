import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the Treeview widget
        self.tree = ttk.Treeview(self, selectmode='browse', columns=('description', 'active'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('description', text='Description')
        self.tree.heading('active', text='Active')
        self.tree.column('description', width=200, anchor='w')
        self.tree.column('active', width=50, anchor='w')

        # Add some dummy data
        for i in range(1, 6):
            self.tree.insert('', 'end', text=f'Item {i}', values=('Description', True))

        # Create the update button
        self.update_button = tk.Button(self, text='Update', command=self.update_item)

        # Pack the widgets
        self.tree.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.update_button.grid(row=0, column=1, sticky='e', padx=5, pady=5)

    def update_item(self):
        # Get the selected item's values
        item_id = self.tree.focus()
        description = self.tree.item(item_id, 'values')[0]
        active = self.tree.item(item_id, 'values')[1]

        # Create the update window
        self.update_window = tk.Toplevel(self)
        self.update_window.title('Update Item')

        # Populate the update window with the selected item's values
        self.description_var = tk.StringVar(value=description)
        self.active_var = tk.BooleanVar(value=active)

        description_label = tk.Label(self.update_window, text='Description:', anchor='w')
        description_entry = tk.Entry(self.update_window, textvariable=self.description_var)

        active_label = tk.Label(self.update_window, text='Active:', anchor='w')
        active_checkbutton = tk.Checkbutton(self.update_window, variable=self.active_var)

        # Create the update and cancel buttons
        update_button = tk.Button(self.update_window, text='Update', command=self.do_update)
        cancel_button = tk.Button(self.update_window, text='Cancel', command=self.update_window.destroy)

        # Grid the widgets
        description_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        description_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        active_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        active_checkbutton.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        update_button.grid(row=2, column=0, sticky='e', padx=5, pady=5)
        cancel_button.grid(row=2, column=1, sticky='w', padx=5, pady=5)

    def do_update(self):
        # Update the selected item in the Treeview
        item_id = self.tree.focus()
        self.tree.item(item_id, values=(self.description_var.get(), self.active_var.get()))
        self.update_window.destroy()

app = App()
app.mainloop()
