import tkinter as tk
from tkinter import ttk

class Header(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self, text="TEST RUNNER")
        label.grid(row=0, column=0)