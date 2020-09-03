# https://medium.com/@javalianimesh/building-tools-with-python-5e38fe348a47
# https://realpython.com/command-line-interfaces-python-argparse/
import argparse
parser= argparse.ArgumentParser(description='This is a tool.')

from tkinter import *
# Create a root window
window= Tk()
window.title('Beautiful Tool')
# Create a window of dimension 500x500. With 400 units on X-axis and 50 units on Y-axis.
window.geometry('500x500+400+50')

# Add Labels to display messages on UI.
label = Label(window, text = 'This is a beautiful Tool! Add your thoughts.')
label.pack()
# Add Entry to input string from users.
entry_line = Entry(window)
entry_line.pack()
# Add Buttons to your UI.
button = Button(window,text = 'Click', width=25)
button.pack()
'''
Add your logic.
'''
# Run this forever.
window.mainloop()