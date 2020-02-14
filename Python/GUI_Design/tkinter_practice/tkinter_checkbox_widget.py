import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')

check_button = ttk.Checkbutton(root, text="Check me!")
check_button.pack()

selected_option = tk.StringVar()

# -- All options --

selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())

check = tk.Checkbutton(
    root,
    text="Check Example",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
)

check.pack()


root.mainloop()