#Tkinter tkmessagebox showinfo()
from Tkinter import *
import tkMessageBox

root = Tk()
tkMessageBox.showinfo("title", "This is awesome")
response = tkMessageBox.askquestion("Question1","Do you like coffee?")
if response == "yes":
    print("Cool")
elif response == "no":
    print("Why not?")
root.mainloop()