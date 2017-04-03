from Tkinter import *
root = Tk()
label1 = Label(root, text = "Label1", bg = "Red", fg = "White")
label1.pack(fill = X)

label2 = Label(root, text = "Label2", bg = "Blue", fg = "White")
label2.pack(side = LEFT, fill = Y)
root.mainloop()