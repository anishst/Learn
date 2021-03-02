import tkinter as tk
import threading
import time



def download():
    while True:
        time.sleep(1)
        print('tick tock')

def stop(): # stop button to close the gui and should terminate the download function too
   root.destroy()

def downloadbutton():
    t = threading.Thread(target=download)
    t.daemon = True
    t.start()

root = tk.Tk()
btn = tk.Button(text = "Start", command=downloadbutton)
btn.pack()
btn = tk.Button(text = "Stop", command=stop)
btn.pack()
root.mainloop()