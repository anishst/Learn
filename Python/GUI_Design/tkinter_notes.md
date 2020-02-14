# Tkinter


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
btn = ttk.Button(root, text="Choices", command=select)
btn.pack(side='left', fill='both', expand=True)
```

## Frames

```
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)
app_header_label = tk.Label(main, text="Selenium Test Runner", bg="navy", fg="white")
app_header_label.pack(side="top",ipadx=10, ipady=10, fill="both", expand=True)
```


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



