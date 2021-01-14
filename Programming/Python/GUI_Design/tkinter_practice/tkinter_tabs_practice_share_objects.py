import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

# shared objects

def on_tab_selected(event): # accept the event arg
	selected_tab = event.widget.select()
	tab_text = event.widget.tab(selected_tab, "text")
	print(f"Selected tab name: {tab_text}")

def get_button(frame):
	programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

	top_frame = tk.Frame(frame, bg='cyan', width=450, height=50, pady=3)
	ttk.Button(top_frame, text="I am a shared button").grid(row=0, column=0)
	return top_frame

tabControl.bind("<<NotebookTabChanged>>", on_tab_selected)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

#  tab 1
ttk.Label(tab1,text ="Welcome to GeeksForGeeks").grid(column = 0, row = 0, padx = 30, pady = 30)
mybutton = get_button(tab1)
mybutton.grid(column = 0, row = 1)
#  TAB 2
ttk.Label(tab2,	text ="Lets dive into the world of computers").grid(column = 0,	row = 0,padx = 30,pady = 30)

mybutton = get_button(tab2)
mybutton.grid(column = 0, row = 1)

root.mainloop()
