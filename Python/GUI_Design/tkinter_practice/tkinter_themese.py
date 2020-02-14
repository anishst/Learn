import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def greet():
    print("Hello!")

root = tk.Tk()
root.geometry('600x400')

style = ttk.Style(root)
# print themes available on the machine
print(style.theme_names())
# show current them
print(style.theme_use())

# change theme
print(style.theme_use('alt'))

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack()

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()