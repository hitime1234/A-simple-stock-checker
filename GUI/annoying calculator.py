#hello am first year in a level computer science this will be calculator with a bunch of math jokes.
global button_presses,result
button_presses =[]
result = 0
from tkinter import *
import time
class windowmanage:
    def createwindow():
        global result,heading
        root = Tk()
        window_size = "500x500"
        root.title("Real and totally normal calculator")
        root.geometry(window_size)
        heading = Label(root,
                        text="enter a calculation",
                        font=("arial",24,"bold"),fg = "black")
        heading.pack()
        return root
    
    def head(window,text,methtod,operator):
        sett = False
        global result,heading
        holdTextCheck = "hahaha the joke is "
        holdTextCheck = holdTextCheck + "if this exist 1=2 would be possible."
        heading.pack()
        if str(result) == holdTextCheck:
            window_size = "900x500"
            window.geometry(window_size)
            window.after(1500, lambda: window.geometry("500x500"))
        elif str(result) == "temp": print("test")
        elif str(window) == "window":
            result = text
    
        if(str(method[1]) ==  "5" or method[0] == "5"): sett = True
        try:
            if (int(result) <= 10 and str(window) != "window"
            and str(text) =="text"):
                window_size = "500x500"
                window.geometry(window_size)
                window.after(3000, lambda: window.geometry("500x500"))
                result = "really you can do\nthis on your fingers ("
                result = result +  str(result) +")"
        except:
            print("\n")
        if  (sett  == True and str(window) != "window"
        and str(text) == "text" and str(operator) == "*"):
            window_size = "500x500"
            window.geometry(window_size)
            window.after(3000, lambda: window.geometry("500x500"))
            result = "Simple trick for multiples of 5?\n Times it by 10,"
            result = result + "\n THEN HALF IT ("  +  str(result) +")"
        if (str(method[1]) == "2" and str(window) != "window"
            and str(text) == "text" and str(operator) == "/"):
            window_size = "1300x500"
            window.geometry(window_size)
            window.after(3000, lambda: window.geometry("500x500"))
            result = "Now, if you really need to know how to divide by 2,\n I"
            result = result + "think you need\n to go back to highschool. ("
            result = result +  str(result) +")"
        if (str(method[1]) == "1" and str(window) != "window"
            and str(text) == "text" and str(operator) == "/"):
            window_size = "500x500"
            window.geometry(window_size)
            window.after(3000, lambda: window.geometry("500x500"))
            result = "...Dividing by 1?\nLook at the other number.("
            result  = result +  str(result) +")"
        elif (str(method[1]) == "1" and str(window) != "window"
              and str(text) == "text" and str(operator) == "/"):
            window_size = "500x500"
            window.geometry(window_size)
            window.after(3000, lambda: window.geometry("500x500"))
            result = "Yes. That was the answer. No.\n"
            result = result + "You didn't need to check it."
            result = result + "("+  str(result) +")"
        

        if str(result) == "69":
            result  = "cheatcode"

            
        heading["text"] = result
        result = ""

    def buttons(window):
        #math symbols
        add = Button(window,text="+",width=10,height=3,bg="lightblue",
                     command=lambda:
                     calculator.appendaction(-1)).place(x=400,y=150)
        subtract = Button(window,text="-",width=10,height=3,bg="lightblue",
                          command=lambda:
                          calculator.appendaction(-2) ).place(x=400,y=225)
        multply = Button(window,text="*",width=10,height=3,bg="lightblue",
                         command=lambda:
                         calculator.appendaction(-4)).place(x=400,y=300)
        divide = Button(window,text="/",width=10,height=3,bg="lightblue",
                        command=lambda:
                        calculator.appendaction(-3)).place(x=400,y=375)
        equal = Button(window,text="=",width=25,height=3,bg="lightblue",
                       command=calculator.calculation).place(x=300,y=440)
        #numbers
        zero = Button(window,
                      text="0",
                      width=15,
                      height=3,
                      bg="lightblue",
                      command=lambda:
                      calculator.appendaction(0)).place(x=50,y=440)
        one = Button(window,
                     text="1",
                     width=10, height=3,bg="lightblue",command=lambda:
                     calculator.appendaction(1)).place(x=75,y=375)
        two = Button(window,
                     text="2",
                     width=10,
                     height=3,
                     bg="lightblue",
                     command=lambda:
                     calculator.appendaction(2)).place(x=175,y=375)
        three = Button(window,text="3",width=10,height=3,bg="lightblue",
                       command=lambda:
                       calculator.appendaction(3)).place(x=275,y=375)
        four = Button(window,text="4",width=10,height=3,bg="lightblue",
                      command=lambda:
                      calculator.appendaction(4)).place(x=75,y=300)
        five = Button(window,text="5",width=10,height=3,bg="lightblue",
                      command=lambda:
                      calculator.appendaction(5)).place(x=175,y=300)
        six = Button(window,text="6",width=10,height=3,bg="lightblue",
                     command=lambda:
                     calculator.appendaction(6)).place(x=275,y=300)
        seven = Button(window,
                       text="7",
                       width=10, height=3,
                       bg="lightblue",
                       command=lambda:
                       calculator.appendaction(7)).place(x=75,y=225)
        eight = Button(window,
                       text="8",
                       width=10,
                       height=3,
                       bg="lightblue",
                       command=lambda:
                       calculator.appendaction(8)).place(x=175,y=225)
        nine = Button(window,
                      text="9",
                      width=10,
                      height=3,
                      bg="lightblue",
                      command=lambda:
                      calculator.appendaction(9)).place(x=275,y=225)
class calculator:
    def appendaction(action):
        try:
            #checks for start
            check1 = len(button_presses) == 0 and int(action) < 0           
            if ("-1" in button_presses or "-2" in button_presses
                or  "-3" in button_presses or "-4" in button_presses):
                if  (-1 == action or -2 == action
                    or  -3 == action or -4 == action):
                    #throw exception
                    int(x)
                else:
                    button_presses.append(str(action))
            elif check1:
                #throw exception
                int(x)
            else:
                button_presses.append(str(action))
        except Exception as e: print("new row needed")
        stringhold = ""
        hold = ""
        key = [" + "," - "," / "," x "]
        if "-1" in button_presses:
            hold = key[0]
            stringhold = ''.join(button_presses)
            stringhold = stringhold.split("-1")
        if "-2" in button_presses:
            hold = key[1]
            stringhold = ''.join(button_presses)
            stringhold = stringhold.split("-2")
        if "-3" in button_presses:
            hold = key[2]
            stringhold = ''.join(button_presses)
            stringhold = stringhold.split("-3")
        if "-4" in button_presses:
            hold = key[3]
            stringhold = ''.join(button_presses)
            stringhold = stringhold.split("-4")
        
        if hold == "":
            stringhold = ''.join(button_presses)

        elif len(stringhold) == 1 and hold != "":
            stringhold = stringhold[0] + hold
        if len(stringhold) == 2:
            stringhold = stringhold[0] + hold + stringhold[1]
        windowmanage.head("window",stringhold,"NULL","NULL")
    def calculation():
        try:
            global button_presses,window,result
            stringhold = ["00","00"]
            if len(button_presses) == 0:
                result = "you dummy you don't know"
                result = result + " what zero is it's middle of number line"
            key = ["+","-","/","*"]
            hold = "+"
            if "-1" in button_presses:
                hold = key[0]
                stringhold = ''.join(button_presses)
                stringhold = stringhold.split("-1")
            if "-2" in button_presses:
                hold = key[1]
                stringhold = ''.join(button_presses)
                stringhold = stringhold.split("-2")
            if "-3" in button_presses:
                hold = key[2]
                stringhold = ''.join(button_presses)
                stringhold = stringhold.split("-3")
            if "-4" in button_presses:
                hold = key[3]
                stringhold = ''.join(button_presses)
                stringhold = stringhold.split("-4")
            if stringhold[0][0] == "0" and len(stringhold[0]) > 1:
                stringhold[0] = stringhold[0][1]
            if stringhold[1][0] == "0"  and len(stringhold[1]) > 1:
                stringhold[1] = stringhold[1][1]
            store = (str("float( ") + stringhold[0]
                     + " "  + hold +  " " + str(stringhold[1])  + " )")
            holdresult = False
            try:
                holdresult = (store.index("/") == NONE
                              and store[store.index("/")+1] == 0) 
            except:
                print("\n")
            if holdresult == False:
                result = eval(store)
            else:
                result = "hahaha the joke is if this exist 1=2"
            button_presses = []
            windowmanage.head(window,"text",stringhold,hold)
        except Exception as e:
           print(e)
           result = "hahaha the joke is if this exist 1=2 would be possible."
           button_presses = []
           windowmanage.head(window,"text",stringhold,hold)
global window
window = windowmanage.createwindow()
windowmanage.buttons(window)
window.mainloop()
