# from tkinter import *
#
# root = Tk()
#
#
# frame1 = Frame(root)
# frame1.place(x = 10, y = 5,width=100,height=100) # Position of where you would place your listbox
# frame1a=Frame(master=frame1)
# frame1a.place(x=0,y=0,height=100,width=100)
#
#
# lb = Listbox(frame1a, width=50, height=6)
# lb.grid(row=0,column=0 )
#
# scrollbar = Scrollbar(frame1, orient="vertical",command=lb.yview)
# scrollbar.pack(side="right", fill="y")
#
#
# lb.config(yscrollcommand=scrollbar.set)
#
# for i in range(10):
#     lb.insert(END, 'test'+str(i))
#
# root.mainloop()

# ============================================================================

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("240x180+130+180")
root.title('listbox with scrollbar')

# create the listbox (height/width in char)
listbox = tk.Listbox(root, width=20, height=6)
listbox.grid(row=0, column=0)

# create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky='ns')
listbox.configure(yscrollcommand=yscroll.set)

# create a vertical scrollbar to the right of the listbox
xscroll = tk.Scrollbar(command=listbox.xview, orient=tk.HORIZONTAL)
xscroll.grid(row=1, column=0, sticky='EW')
listbox.configure(xscrollcommand=xscroll.set)

# now load the listbox with data
friend_list = [
'Stew', 'Tom', 'Jen', 'Adam', 'EthelWSFSFFFFFFFFFFFFFFFFFF', 'Barb',   'Tiny',
'Tim', 'Pete', 'Sue', 'Egon', 'Swen', 'Albert']
for item in friend_list:
    # insert each new item to the end
    # of the listbox
    listbox.insert('end', item)

# optionally scroll to the bottom of the listbox
lines = len(friend_list)
listbox.yview_scroll(lines, 'units')

root.mainloop()

# ==========================================================================================

# controlling-two-text-widgets-with-one-scrollbar

# try:
#     from Tkinter import *
# except ImportError:  ## Python 3
#     from tkinter import *

# root = Tk()
#
#
# class App:
#     def __init__(self, master):
#         scrollbar = Scrollbar(master, orient=VERTICAL)
#         self.b1 = Text(master, yscrollcommand=scrollbar.set)
#         self.b2 = Text(master, yscrollcommand=scrollbar.set)
#         scrollbar.config(command=self.yview)
#         scrollbar.pack(side=RIGHT, fill=Y)
#         self.b1.pack(side=LEFT, fill=BOTH, expand=1)
#         self.b2.pack(side=LEFT, fill=BOTH, expand=1)
#
#     def yview(self, *args):
#         self.b1.yview(*args)
#         self.b2.yview(*args)
#
#
# app = App(root)
#
# for item in range(0, 40):
#     for i in range(item):
#         it = str(i) + ' '
#         app.b1.insert(1.0, it)
#         app.b2.insert(1.0, it)
#     app.b1.insert(1.0, '\n')
#     app.b2.insert(1.0, '\n')
#
# root.mainloop()