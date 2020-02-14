import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=8)
text.grid(row=0, column=0, sticky="EW")
text.insert("1.0", "Please enter some...")

text_scroll = ttk.Scrollbar(root,orient="vertical", command=text.yview())
text_scroll.grid(row=0, column=1, sticky="ns")
text["vscrollcommand"] = text_scroll.set

root.mainloop()