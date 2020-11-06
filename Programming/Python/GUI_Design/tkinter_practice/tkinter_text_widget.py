import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')

# simple text
text = tk.Text(root, height=5)
text.pack()

# insert content = 1.0  1=line num ; 0 char number
text.insert("1.0", "please enter a comment...")
# disable text area
text["state"] = "normal"  # use "disabled"

# get text from start to end
txt_content = text.get("1.0", "end")
print(txt_content)

root.mainloop()