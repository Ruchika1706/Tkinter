#Canvas to draw something
from Tkinter import *
import tkMessageBox
root = Tk()


canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

#draw a line on the canvas (0,0) is the top most corner of the screen
newline = canvas.create_line(0, 0, 100, 100)
otherline = canvas.create_line(10, 10, 50, 150, fill = "green")
rectangle = canvas.create_rectangle(100, 100, 130, 130, fill = "red")


root.mainloop()