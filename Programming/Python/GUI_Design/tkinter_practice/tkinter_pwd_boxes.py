from tkinter import  *

class GetPassword(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body(self)

    def body(self, master):
        self.title("Enter New Password")
        Label(master, text='Old Password:').grid(row=0, sticky=W)
        Label(master, text='New Password:').grid(row=1, sticky=W)
        Label(master, text='Enter New Password Again:').grid(row=2,
        sticky=W)
        self.oldpw = Entry(master, width = 16, show='*')
        self.newpw1 = Entry(master, width = 16, show='*')
        self.newpw2 = Entry(master, width = 16, show='*')
        self.oldpw.grid(row=0, column=1, sticky=W)
        self.newpw1.grid(row=1, column=1, sticky=W)
        self.newpw2.grid(row=2, column=1, sticky=W)


root = GetPassword()
root.mainloop()