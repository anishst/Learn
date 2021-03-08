import threading
from threading import Event
import time
from tkinter import Tk, Button


root = Tk()

class Control(object):

    def __init__(self):
        self.my_thre
        ad = None
        self.stopThread = False

    def just_wait(self):
        print(f"Counting 0 to 10000")
        for i in range(10000):
            if self.stopThread:
                print("Stopping the thread")
                self.stopThread = False
                break  # early termination
            time.sleep(1)
            print(i)

    def button_callback(self):
        self.my_thread = threading.Thread(target=self.just_wait)
        self.my_thread.start()

    def button_callbackStop(self):
        self.stopThread = True
        self.my_thread.join()
        self.my_thread = None


control = Control()
button = Button(root, text='Run long thread.', command=control.button_callback)
button.pack()
button2 = Button(root, text='stop long thread.', command=control.button_callbackStop)
button2.pack()


root.mainloop()