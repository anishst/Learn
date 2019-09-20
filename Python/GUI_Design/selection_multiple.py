from tkinter import *
from tkinter import ttk

main = Tk()
main.title("Selenium Test Cases")
main.geometry("+50+150")
frame = ttk.Frame(main, padding=(3, 3, 12, 12))
frame.grid(column=0, row=0, sticky=(N, S, E, W))

tests = StringVar()
tests.set("CIRAQuery CreateMVD SearchDeposits")

lstbox = Listbox(frame, listvariable=tests, selectmode=MULTIPLE, width=20, height=10)
lstbox.grid(column=0, row=0, columnspan=2)

def select():
    reslist = list()
    seleccion = lstbox.curselection()
    for i in seleccion:
        selected_tests = lstbox.get(i)
        reslist.append(selected_tests)
    for val in reslist:
        print(val)

btn = ttk.Button(frame, text="Choices", command=select)
btn.grid(column=1, row=1)

main.mainloop()