import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SC")
        self.geometry('400x500')
        self.resizable(width=False, height=False)

        names = ['Title', 'Graphs', 'Messages', 'Instructions', 'new']
        self.nb = self.create_notebook(names)
        self.menu = self.create_menus()

        # We can also add items to the Notebook here
        tab = self.nb.tabs['Instructions']
        tk.Label(tab, text='You should\nread these\ninstructions').pack()

        self.mainloop()

    def create_notebook(self, names):
        nb = MyNotebook(self, names)
        nb.pack()

        def add_label(parent, text, row, column):
            label = tk.Label(parent, text=text)
            label.grid(row=row, column=column, sticky=tk.N, pady=10)
            return label

        # Add some labels to each tab
        tab = nb.tabs['Title']
        for i in range(3):
            add_label(tab, 't' + str(i), i, 0)

        tab = nb.tabs['Graphs']
        for i in range(3):
            add_label(tab, 'g' + str(i), 0, i)

        tab = nb.tabs['Messages']
        for i in range(3):
            add_label(tab, 'm' + str(i), i, i)

        return nb

    def create_menus(self):
        menu = tk.Menu(self, tearoff=False)
        self.config(menu=menu)
        subMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_separator()
        subMenu.add_command(label='Exit', command=self.destroy)
        return menu

class MyNotebook(ttk.Notebook):
    ''' A customised Notebook that remembers its tabs in a dictionary '''
    def __init__(self, master, names):
        super().__init__(master, width=390, height=470)

        # Create tabs & save them by name in a dictionary
        self.tabs = {}
        for name in names:
            self.tabs[name] = tab = ttk.Frame(self)
            self.add(tab, text=name)

GUI()