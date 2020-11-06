import tkinter as tk


master = tk.Tk()
master.title("Widget Examples")
tk.Label(master, text="First").grid(row=0, sticky='W')
tk.Label(master, text="Second").grid(row=1, sticky='W')

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()