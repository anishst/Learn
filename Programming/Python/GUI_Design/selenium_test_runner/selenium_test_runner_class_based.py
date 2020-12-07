import threading
import time
import tkinter as tk
from tkinter import ttk


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


class Header(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self, text="TEST RUNNER")
        label.grid(row=0, column=0)


class Contents(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name: ")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, text="Run Selected Tests ", command=self.submit)
        # progressbar = ttk.Progressbar(self, mode='indeterminate')
        self.status_label = ttk.Label(self, text="Choose")

        label.grid(row=0, column=0, sticky="E")
        entry.grid(row=1, column=0,sticky="E" ,padx=5, pady=5)
        button.grid(row=2, column=0)
        self.status_label.grid(column=0, row=3, sticky='W')

        self.stop_button = ttk.Button(
            self,
            text="Stop",
            cursor="hand2"
        )

        self.quit_button = ttk.Button(
            self,
            text="Quit",
            state="enabled",
            command=self.quit,
            cursor="hand2"
        )
        self.stop_button.grid(row=2, column=1, sticky="E", padx=5)
        self.quit_button.grid(row=2, column=2, sticky="E", padx=5)

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")

    def submit(self):
        print("Code is running...")
        self.status_label.configure(text="Running Tests....")
        self.update()
        time.sleep(5)  # put your stuff here
        self.status_label.configure(text="Test Completed!")
        self.update()




root = HelloWorld()
root.mainloop()