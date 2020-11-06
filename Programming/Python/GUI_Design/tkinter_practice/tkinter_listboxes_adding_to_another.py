import tkinter as tk
from tkinter import  ACTIVE, END
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Widget Examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

pl = tk.StringVar(value=programming_languages)
pl_select = tk.Listbox(root, listvariable=pl, height=6)
pl_select.pack(padx=10, pady=10)
pl_select["selectmode"] = "extended"

pl2_select = tk.Listbox(root, height=6)
pl2_select.pack(padx=10, pady=10)
pl2_select["selectmode"] = "extended"

def remove_name():
    pl2_select.delete(ACTIVE)

def add_name():
    x = pl_select.get(ACTIVE)
    pl2_select.insert(END, x)

add_button = tk.Button(root, text='Add',
                    command=add_name)
add_button.pack()

remove_button = tk.Button(root, text='Remove',
                    command=remove_name)
remove_button.pack()

def handle_selection_change(event):
    selected_indices = pl_select.curselection()
    for i in selected_indices:
        print(pl_select.get(i))
    e = pl_select.get(0, END)
    print(e)
    print(f"*****added****")
    f = pl2_select.get(0,END)
    print(f)
    # remove dupes
    print(set(list(f)))


pl_select.bind("<<ListboxSelect>>", handle_selection_change)
root.mainloop()