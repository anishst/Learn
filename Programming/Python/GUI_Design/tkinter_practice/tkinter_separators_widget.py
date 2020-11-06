import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')


image = Image.open("python_logo.png").resize((100, 64))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo, padding=5)
label.pack()

# logo and text
label2 = ttk.Label(root, text="Python logo", image=photo, padding=5, compound="right")
label2.pack()

ttk.Separator(root, orient="horizontal").pack(fill='x')
# change label dynamically
greeting = tk.StringVar()
label3 = ttk.Label(root, paddin=10, textvariable=greeting)
label3.pack()
greeting.set("Hello world!")

root.mainloop()