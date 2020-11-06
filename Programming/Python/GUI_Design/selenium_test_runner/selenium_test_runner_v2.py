import tkinter as tk
from tkinter import ttk
from tkinter import  ACTIVE, END
# v2 - changed pack to grid

root = tk.Tk()
# root.geometry("1024x768")
# root.resizable(False,False) # prevent resizing
root.title("OTCNet - Selenium Test Runner")
root.columnconfigure(0, weight=1)

# header frame
header_frame = ttk.Frame(root)
header_frame.grid(sticky="EW")
header_frame.columnconfigure(0, weight=1)
# app title
app_header_label = tk.Label(header_frame, text="Selenium Test Runner", bg="navy", fg="white")
# adjust title font
app_header_label.config(font=("Tahoma", 20))
app_header_label.grid(ipadx=10, ipady=10, sticky="EW")


# browser selection
browser_selection_frame = ttk.Frame(root, padding=(20,10))
browser_selection_frame.grid(sticky="EW")
browser_selection_label = tk.Label(browser_selection_frame, text="Select Browser:")
browser_selection_label.grid(row=1, column=0, ipadx=10, ipady=10, sticky="EW")

browser_variable = tk.StringVar()
option_one = ttk.Radiobutton(browser_selection_frame,text="Chrome",variable=browser_variable,value="chrome")
option_two = ttk.Radiobutton(browser_selection_frame,text="Ie",variable=browser_variable,value="ie")
option_one.grid(row=1, column=1, sticky="EW")
option_two.grid(row=1, column=2, sticky="EW")

# available test cases
test_cases_frame = ttk.Frame(root, padding=(20,10))
test_cases_frame.grid(sticky="EW")
test_cases = ("Test1", "Test2", "Test3", "Test4")
tc_list = tk.StringVar(value=test_cases)
tc_select = tk.Listbox(test_cases_frame, listvariable=tc_list, height=20)
tc_select.grid(row=1, column=1, sticky="EW")
def add():
    selected_value = tc_select.get(ACTIVE)
    # add selection to end of list
    tc_select2.insert(END, selected_value)

def remove():
    # remove selection
    tc_select2.delete(ACTIVE)

add_button = ttk.Button(test_cases_frame, text="Add", command=add)
add_button.grid(row=1, column=2, sticky="EW")
remove_button = ttk.Button(test_cases_frame, text="Remove", command=remove)
remove_button.grid(row=1, column=3, sticky="EW")
# test_cases_added = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")
# tc_list2 = tk.StringVar(value=test_cases_added)
tc_select2 = tk.Listbox(test_cases_frame, listvariable=None, height=20)
tc_select2.grid(row=1, column=4, sticky="EW")


# seperator frame
sep_frame = ttk.Frame(root, padding=(5))
sep_frame.grid(sticky="EW")
sep_frame.columnconfigure(0, weight=1)
sep = ttk.Separator(sep_frame, orient="horizontal")
sep.grid(sticky="EW")



# buttons frame
buttons_frame = ttk.Frame(root, padding=(20,10))
buttons_frame.grid(sticky="EW")
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)
run_tests_btn = ttk.Button(buttons_frame, text="Run Selected Tests")
run_tests_btn.grid(row=1, column=0, sticky="EW")
quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.grid(row=1, column=1, sticky="EW")

root.mainloop()

print(browser_variable.get(), "was selected.")
