from Tkinter import *
root = Tk()
def doSomething():
    print("you clicked the button")



button1 = Button(root, text = "Click here", command = doSomething())
button1.pack()

root.mainloop()