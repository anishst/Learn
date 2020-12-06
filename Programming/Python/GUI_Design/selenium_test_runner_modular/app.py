import threading
import time
import tkinter as tk
from tkinter import ttk
from frames.header import Header
from frames.contents import Contents


class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Selenium Test Runner")
        # self.geometry("1024x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        header_frame = Header(self)
        header_frame.grid(row=0, column=0,sticky="NSEW")

        frame = Contents(self)
        frame.grid(row=1, column=0, sticky="NSEW")
        frame.columnconfigure(0, weight=1)








root = HelloWorld()
root.mainloop()