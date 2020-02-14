# https://stackoverflow.com/questions/37442974/adding-items-from-one-tkinter-listbox-to-another
from tkinter import *

root = Tk()
root.geometry('330x200')

names = ['Bill', 'Jack', 'Joanne', 'Ann', 'Dave', 'Jane']


def add_name():
    x = parent.get(ACTIVE)
    child.insert(END, x)


def remove_name():
    child.delete(ACTIVE)


parent = Listbox(root)
for name in names:
    parent.insert(END, name)

parent.place(x=5, y=5)

add_button = Button(root, text='Add',
                    command=add_name)
add_button.place(x=148, y=5)

remove_button = Button(root, text='Remove',
                       command=remove_name)
remove_button.place(x=138, y=50)

child = Listbox(root)
child.place(x=200, y=5)

root.mainloop()