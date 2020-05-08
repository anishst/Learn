import tkinter as tk
from tkinter import ttk
import _thread

class GUI(tk.Tk):

    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.shouldPrint = True
        self.initialize()

    def lock_func(self):
        while self.shouldPrint:
            print("blah")

    def setShouldPrint(self, value):
        self.shouldPrint = value

    def initialize(self):
        self.processBtn = tk.Button(self, text="Process", command=lambda: _thread.start_new_thread(self.lock_func, ()))
        self.stopBtn = tk.Button(self, text = "Stop", command = lambda: self.setShouldPrint(False))
        self.processBtn.grid(row = 1)
        self.stopBtn.grid(row = 2)


app = GUI(None)
app.mainloop()