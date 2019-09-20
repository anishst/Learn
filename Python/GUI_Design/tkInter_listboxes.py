from tkinter import *

main = Tk()
main.title("Multiple Choice Listbox")
main.geometry("+50+150")

listbox = Listbox(main)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

def ok():
	print(listbox.get(listbox.curselection()))
def quit():
	print("quiting application")
	main.quit()

button = Button(main, text="OK", command=ok)
button.pack()

button = Button(main, text="Quit", command=quit)
button.pack()

mainloop()