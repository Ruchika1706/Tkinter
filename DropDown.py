#Usage of class to create User Interface
#Creation of Menu and MenuItems.
#We already have a class for Menu
from Tkinter import *
def function1():
    print("Menu Item Clicked")
root = Tk()

#Creation of Menu Object
mymenu = Menu(root)
root.config(menu = mymenu)

#Add menu object to the root configuration


#Pass main menu to this sub menu
#Creation of submenu object
filemenu = Menu(mymenu)

mymenu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = " New Project", command = function1)

filemenu.add_separator() # to have a separator file for classification of menu items

filemenu.add_command(label = " Save", command = function1)


editmenu = Menu(mymenu)
mymenu.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Copy", command = function1)

editmenu.add_separator() # to have a separator file for classification of menu items

editmenu.add_command(label = "Paste", command = function1)








root.mainloop()