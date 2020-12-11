# Tkinter

Standard Python interface to the Tk GUI toolkit for creating GUI apps
- consists of widgets
    - Frame: for providing a structure to your application
    - Buttons: used for taking input from the user
    - Checkbuttons: used for making selections
    - Labels: for displaying textual information
    - File Dialogs: for uploading or downloading files to/from the application
    - Canvas: provides a space for drawing/painting things like graphs and plots


## Set screen size

```python
import tkinter as tk
root = tk.Tk()
root.geometry('600x400')
root.mainloop()
```
## Buttons

```python

from tkinter import ttk
import tkinter as tk
root = tk.Tk()
btn = ttk.Button(root, text="Choices")
btn.pack(side='left', fill='both', expand=True)
```

### Using commands
```python
# using lamda
def button_click(number):
    return None

from tkinter import ttk
import tkinter as tk
root = tk.Tk()
btn = ttk.Button(root, text="Choices", command=button_click)
btn.pack(side='left', fill='both', expand=True)


btn = ttk.Button(root, text="Choices", command=lambda: button_click("1"))
```
## Entry/Textbox

```python

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")
# get value in entry 
input_val = e.get()
# delete
e.delete(0, END)
```
## Frames

```
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)
app_header_label = tk.Label(main, text="Selenium Test Runner", bg="navy", fg="white")
app_header_label.pack(side="top",ipadx=10, ipady=10, fill="both", expand=True)
```

### Label Frame

```python
class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
 
        self.title("Tkinter Label Frame")
        self.minsize(600,400)
        self.wm_iconbitmap('icon.ico')
 
 
        self.labelFrame = ttk.LabelFrame(self, text = "Label Frame")
        self.labelFrame.grid(column = 0, row = 7, padx = 20, pady = 40)
 
 
        self.labels()
```        
## Notebook

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')


n = ttk.Notebook(root)
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
n.add(f1, text="Stab")
n.add(f2, text="Regression")
n.pack()
root.mainloop()
```

## Images

```python
from PIL import ImageTk,Image
my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_label = Label(image=my_img)
my_label.pack()
```
## Message boxes

https://docs.python.org/3/library/tkinter.messagebox.html


## Pack vs Grid

Grid is preferred; allows more control

## windows high resolution fix

```python
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
    print("dpi fix didn't work")
```


## Resources

- https://tkdocs.com/tutorial/grid.html
- https://www.geeksforgeeks.org/introduction-to-tkinter/?ref=lbp
- https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
- Video tutorials:
    - Tkinter
        - https://youtu.be/YXPyB4XeYLA
            - [git repo]( https://www.youtube.com/redirect?q=https%3A%2F%2Fgithub.com%2Fflatplanet%2FIntro-To-TKinter-Youtube-Course&v=YXPyB4XeYLA&redir_token=QUFFLUhqblZSSjQ1ZU9YRWNRSTltbkN0X3pMMzZmR0xGd3xBQ3Jtc0ttNVJBeGhMRzFRQVVCcFhOSmdRamNOM2N2a0tLZGZHQVV0bF82Q1hrem14aHlueFBSamxDZThWaExLajh2cGF4N2MxN1ptLWFkMWtNb3RSUTBwRURSdFNNQklkTUFIQktvR01NQkRPbEtHYi1YTTFGWQ%3D%3D&event=video_description)
    - Kivy
        - Kivy Tutorial: https://www.youtube.com/watch?v=bMHK6NDVlCM&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn
    - PyQT
        - https://youtu.be/Vde5SH8e1OQ
    - wxPython
        - https://www.youtube.com/watch?v=NMjV_HGLAQE
     - more : https://towardsdatascience.com/top-10-python-gui-frameworks-for-developers-adca32fbe6fc
- Git Repos
    - [git repo]( https://www.youtube.com/redirect?q=https%3A%2F%2Fgithub.com%2Fflatplanet%2FIntro-To-TKinter-Youtube-Course&v=YXPyB4XeYLA&redir_token=QUFFLUhqblZSSjQ1ZU9YRWNRSTltbkN0X3pMMzZmR0xGd3xBQ3Jtc0ttNVJBeGhMRzFRQVVCcFhOSmdRamNOM2N2a0tLZGZHQVV0bF82Q1hrem14aHlueFBSamxDZThWaExLajh2cGF4N2MxN1ptLWFkMWtNb3RSUTBwRURSdFNNQklkTUFIQktvR01NQkRPbEtHYi1YTTFGWQ%3D%3D&event=video_description)
    

