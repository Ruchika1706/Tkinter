from Tkinter import *
def function1():
    print("Menu Item Clicked")
root = Tk()
toolbar = Frame(root, bg = "RED")
button1 = Button(toolbar, text = "click Me", command = function1)
button1.pack(side = LEFT, padx = 2, pady = 3)

button2 = Button(toolbar, text = "Print", command = function1)
button2.pack(side = LEFT, padx = 2, pady = 3)
toolbar.pack(side = TOP, fill = X)
root.mainloop()