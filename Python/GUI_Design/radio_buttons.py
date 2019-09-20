from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   if str(var.get()) == '1':
      print("You selected option 1")
      from selenium import webdriver
      import time

      driver = webdriver.Chrome()
      driver.get("https://www.google.com") 
      driver.find_element_by_name('q').send_keys("Cheese") 
      time.sleep(5)
      driver.quit()   


root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Chrome", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="IE", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Firefox", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()