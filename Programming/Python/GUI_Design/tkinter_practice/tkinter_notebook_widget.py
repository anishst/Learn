import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')

n = ttk.Notebook(root)
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
n.add(f1, text="Stab")
n.add(f2, text="Regression")
n.pack()
root.mainloop()