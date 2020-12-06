# https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button

import os
import time
from datetime import datetime
import shutil
import threading
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
frame = tk.Frame(root)
button = tk.Button(frame, text="Check", command=lambda:start_submit_thread(None))

def submit():
    print("Code is running...")
    time.sleep(10) # put your stuff here
    print("Code is finished!")



def start_submit_thread(event):
    global submit_thread
    button.configure(state='disabled')
    submit_thread = threading.Thread(target=submit)
    submit_thread.daemon = True
    progressbar.start()
    submit_thread.start()
    root.after(5, check_submit_thread)

def check_submit_thread():
    if submit_thread.is_alive():
        # print("checking status of thread")
        root.after(5, check_submit_thread)

    else:
        progressbar.stop()
        print("Progress bar stopped!")
        button.configure(state="normal")

def stop_thread():
    pass
    # https://stackoverflow.com/questions/22596975/terminate-the-thread-by-using-button-in-tkinter

frame.pack()
progressbar = ttk.Progressbar(frame, mode='indeterminate')
progressbar.grid(column=1, row=0, sticky='W')

# tk.Button(frame, text="Check", command=lambda:start_submit_thread(None)).grid(column=0, row=1,sticky='E')

button.grid(column=0, row=1,sticky='E')
# button.configure(state='disabled')
root.mainloop()