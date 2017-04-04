#Usage of class to create User Interface
from Tkinter import *
class MyButtons:
    def __init__(self, rootone):
        frame = Frame(rootone) # Add a frame on our root window
        frame.pack()
        self.button1 = Button(frame, text = "Click Me", command = self.printMsg)
        self.button1.pack()
        self.button2 = Button(frame, text = "Exit", command = frame.quit) #frame.quit inbuilt method to exit the window
        self.button2.pack(side = TOP)

    def printMsg(self):
        print("wow you clicked me")


root = Tk()
temp = MyButtons(root)
root.mainloop()