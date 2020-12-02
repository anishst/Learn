# https://blog.tecladocode.com/tkinters-grid-geometry-manager/
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
#  Make the row stretch all the way down
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="NSEW")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.grid(column=1, row=0, ipadx=10, ipady=10, sticky="NSEW")

rectangle_3 = tk.Label(root, text="Rectangle 1", bg="orange", fg="white")
rectangle_3.grid(column=0, row=1, columnspan=2, ipadx=10, ipady=10, sticky="NSEW")

root.mainloop()