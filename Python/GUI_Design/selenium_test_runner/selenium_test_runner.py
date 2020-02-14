import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.geometry("1024x768")
root.title("Selenium Test Runner - Anish")

# header frame
header_frame = ttk.Frame(root)
header_frame.pack(fill="both")
# app title
app_header_label = tk.Label(header_frame, text="Selenium Test Runner", bg="navy", fg="white")
app_header_label.pack(side="left",ipadx=10, ipady=10, fill="both", expand=True)


# buttons frame
buttons_frame = ttk.Frame(root, padding=(20,10))
buttons_frame.pack(fill="both")

run_tests_btn = ttk.Button(buttons_frame, text="Run Selected Tests")
run_tests_btn.pack(side="left", fill="x", expand=True)
quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop()