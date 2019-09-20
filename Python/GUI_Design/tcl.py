# https://wiki.python.org/moin/TkInter
# http://effbot.org/tkinterbook/tkinter-whats-tkinter.htm
# https://www.python-course.eu/tkinter_labels.php


# example 1
# from tkinter import *
# root = Tk()
# w = Label(root, text="Hello, world!")
# w.pack()
# root.mainloop()

# example 2

# import tkinter as tk

# counter = 0 
# def counter_label(label):
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
 
 
# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()



# example 3

from tkinter import *

master = Tk()

var = StringVar(master)
var.set("one") # initial value

option = OptionMenu(master, var, "one", "two", "three", "four")
option.pack()

#
# test stuff

def ok():
    print ("value is", var.get())
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()