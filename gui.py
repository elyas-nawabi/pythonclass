# env
# cli: command line interface
# gui: graphical user interface
from tkinter import *

myWindow = Tk()
myWindow.title("My Player")
addButton = Button(myWindow, text="Login")
addButton.place(x = 50, y = 70)
myWindow.mainloop()

