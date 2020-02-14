import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def greet():
    print("Hello!")

root = tk.Tk()
root.geometry('600x400')

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack()

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()