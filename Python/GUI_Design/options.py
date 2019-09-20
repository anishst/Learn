from tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

var = StringVar()
label = Label( master, textvariable=var, relief=RAISED )
label.pack()

var.set("Hey!? How are you doing?")

def ok():
    print ("value is", variable.get())
    var.set(variable.get())
    # master.quit()
button = Button(master, text="OK", command=ok)
button.pack()
mainloop()