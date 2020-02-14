import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Widget Examples")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekday["state"] = "readonly"  # "normal is the counterpart"; prevent user from entering values
weekday.pack()

#  do something when event happens
def handle_selection(event):
    print("Today is", weekday.get())
    print("But we're gonna change it to Friday.")
    weekday.set("Friday")
    print(weekday.current())  # This can return -1 if the user types their own value.


weekday.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()

print(selected_weekday.get(), "was selected.")