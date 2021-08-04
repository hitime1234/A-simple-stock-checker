#gui framework
from tkinter import *
import time
global TokenADD,urlADD
import stockCheck
url = ""
Token =""
def Store(root):
    url = urlADD.get()
    Token = TokenADD.get()
    stockCheck.GUISTARTHANDLE(url,Token,root)
    

class windowmanage:
    def createwindow(header,title1,size):
        global result,heading
        root = Tk()
        try:
            window_size = str(size)
        except:
            window_size = "500x500"
        root.title(str(title1))
        root.geometry(window_size)
        heading = Label(root,
                        text=str(header),
                        font=("arial",24,"bold"),fg = "black")
        heading.pack()
        return root
    
    def textBoxHandler(top):
        Urlenter = Label(top, text="enter the url: ",font = ("arial",11,"bold"),fg="black").place(x=10,y=100)
        Tokenenter = Label(top, text="enter out of stock message: ",font = ("arial",11,"bold"),fg="black").place(x=10,y=140)
        global urlADD 
        urlADD = StringVar()
        global TokenADD
        TokenADD= StringVar()
        entry_box = Entry(top, textvariable=urlADD,width=70,bg="light blue").place(x=50,y=120)
        entry_box2 = Entry(top, textvariable=TokenADD,width=70,bg="light blue").place(x=50,y=165)
         

    

    def createbuttons(window):
        enter = Button(window,text="Start",width=20,height=3,bg="lightblue",
                     command=lambda:
                     Store(window)).place(x=174,y=425)
                        
    
