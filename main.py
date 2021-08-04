#gui main script
global root
from tkinter import *
def MainInput():
    global root
    import GUI
    root = GUI.windowmanage.createwindow("input website to track","website stock tracker","500x500")
    GUI.windowmanage.createbuttons(root)
    GUI.windowmanage.textBoxHandler(root)
    root.mainloop()



    
MainInput()

