#Python GUI
from Tkinter import * # Import it all at once

#First task is to create a window
root = Tk() # Create an object of Tkinter class

#create a label
label1 = Label(root, text="Hello World!") #create a label


#add label to the window, packs up label on the window
label1.pack() #add label to window

#Execution till this point is so fast that you will not be able to see the window.
#To close the appeared window using cross button, for visibility
root.mainloop() #to create the window running