#Usage of class to create User Interface
#Creation of Menu and MenuItems.
#We already have a class for Menu
from Tkinter import *
def function1():
    print("Menu Item Clicked")
root = Tk()

#Creation of Menu Object
mymenu = Menu(root)

#Add menu object to the root configuration


#Pass main menu to this sub menu
#Creation of submenu object
submenu = Menu(mymenu, tearoff = 0)

submenu.add_command(label = " New Project", command = function1)

submenu.add_separator() # to have a separator file for classification of menu items

submenu.add_command(label = " Save", command = function1)

mymenu.add_cascade(label = "File", menu = submenu)

root.config(menu = mymenu)

root.mainloop()