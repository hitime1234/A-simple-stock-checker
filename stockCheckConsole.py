#FOR the people wonder this is not a BOT SCRIPT as per licensing
#PLEASE DON't use this to make one
#this allows people to check stock of somethings
#if there is a problem most likely it could retailing blocking html queries or something blocking network traffic or your don't have internet

import time
import urllib.request as urllib


url = input("URL:\n")
Token =input("\n\nWhat is the out stock message say\ne.g Sorry this item is out of stock\n\n:\n")


#get html bytes then converts to returned string
def getsHtmlString(url):
    try:
        #rate limt
        time.sleep(0.25)
        re = urllib.urlopen(url).read().decode()
    except:
        re = -1
    return re


#finds if the data contains the out of stock message
def FindToken(re,Token):
    try:
        if re.find(Token) == -1:
            print("the item is in stock")
        else:
            print("the item isn't in stock")
        
    except:
        print("problem searching check the url")
#--mathea the snow fox lover
#https://github.com/hitime1234
print("\n\n\n")

while True:
    htmlData =getsHtmlString(url)
    FindToken(htmlData,Token)



