#A frame is a container to hold your widgets. Window is also container. Windo contains frames

from Tkinter import *
root = Tk()
newframe = Frame(root)
newframe.pack()
newframe1 = Frame(root)
newframe1.pack(side = BOTTOM)
button1 = Button(newframe, text= "Click Me", fg = "RED")
button2 = Button(newframe1, text= "Click Me", fg = "BLUE")
button1.pack()
button2.pack()
root.mainloop()