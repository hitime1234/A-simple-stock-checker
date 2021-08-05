#FOR the people wonder this is not a BOT SCRIPT as per licensing
#PLEASE DON't use this to make one
#this allows people to check stock of somethings
#if there is a problem most likely it could retailing blocking html queries or something blocking network traffic or your don't have internet
from tkinter import *
from tkinter import messagebox
import time
global var,url,Token,root,breakClause,thread
import threading
breakClause  =  False
def TextBasedInput():
    url = input("URL:\n")
    Token =input("\n\nWhat is the out stock message say\ne.g Sorry this item is out of stock\n\n:\n")


#get html bytes then converts to returned string
def getsHtmlString(url):
    #rate limt
    try:
        import urllib.request as urllib
        req = urllib.Request(
        url, 
        data=None,
        #the goal here is to basically fake a browser GET request so eshops don't 403 error 
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
        "Dnt": "1",
        #fun fact during the making of this I found out some eshops prevent scrappers like this being used by requiring a cookie to given
        'Cookie': 'visid_incap_774904=W2dv4v7LQ9O+mAgXMTXNEkf0wFoAAAAAQUIPAAAAAAAa0bYG0xZT8EYzEjek6QAz; incap_ses_534_774904=hy1MMZjKpnSDJyYmoCZpB0f0wFoAAAAAZA+Th6cYjAoseY9Kq7vrFA==',
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
        })
        re = urllib.urlopen(req).read().decode()
    except Exception as e:
        print(str(e))
        print("there was a problem check the url or import module")
        re = -1
    return re


#finds if the data contains the out of stock message
def FindToken(re,Token):
    try:
        if re.find(Token) == -1:
            return False
        else:
            return True
        
    except:
        print("problem searching check the url")
#--mathea the snow fox lover
#https://github.com/histime1234

def CreateStock(top):
    enter = Label(top, textvariable=var,font = ("Roboto",25,"bold"),fg="black").place(x=10,y=300)
    return enter

def Start():
    global breakClause
    while True:
        try:
            print (time.strftime("%I:%M:%S"))
            htmlData =getsHtmlString(url)
            hold = FindToken(htmlData,Token)
            if hold == True:
                var.set("No stock")
            else:
                var.set("In stock")
            if breakClause == True:
               break
        except:
            if breakClause == True:
               break
        

def on_closing():
    global breakClause,thread
    breakClause = True
    root.destroy()
        

def GUISTARTHANDLE(url1,Token1,root1):
    global var,url,Token,root,thread
    url =  url1
    Token = Token1
    root = root1
    print("\n\n\n")
    var = StringVar()
    var.set("No stock")
    en = CreateStock(root)
    thread = threading.Thread(target=Start)
    thread.daemon = True
    thread.start()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
