import time
import tkinter as tk
from tkinter import ttk
from threading import Thread
from queue import Queue

class Contents(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name: ")
        entry = ttk.Entry(self, textvariable=self.user_input)
        self.button = ttk.Button(self, text="Run Selected Tests ", command=self.create_thread)
        # progressbar = ttk.Progressbar(self, mode='indeterminate')
        self.status_label = ttk.Label(self, text="Choose")

        label.grid(row=0, column=0, sticky="E")
        entry.grid(row=1, column=0,sticky="E" ,padx=5, pady=5)
        self.button.grid(row=2, column=0)
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

    def create_thread(self):
        global run_thread
        self.run_thread = Thread(target=self.submit)
        # run the thread as background task
        self.run_thread.setDaemon(True)
        self.run_thread.start()

    def submit(self):
        self.button.configure(state='disabled')
        print("Code is running...")
        self.status_label.configure(text="Running Tests....")
        self.update()
        time.sleep(5)  # put your stuff here
        self.status_label.configure(text="Test Completed!")
        self.button.configure(state='normal')
        # self.update()
        # self.after(5, self.check_submit_thread)

    def check_submit_thread(self):
        if run_thread.is_alive():
            print("checking status of thread")
            self.after(5, self.check_submit_thread)
        #
        # else:
        #     progressbar.stop()
        #     print("Progress bar stopped!")
        #     button.configure(state="normal")