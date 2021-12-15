# A-simple-stock-checker

# Requirements

  # Console & GUI:
  
  urllib.requests
  
  python 3
  
  #  GUI:
  
  Tkinter 
  
  threading
  
  --note this is changable if a executable package gets made when if feel like it
  

# making your own executable
    download python3 
    open command prompt (windows 7/8/10)
    windows 10 specifically uses this commands
    commands:
        py -m pip install pyinstaller
        cd "to your downloads folder/containing GUI source"
        py -m PyInstaller -F main.py --hidden-import stockCheck --hidden-import GUI -i bulb.ico
    
# ChangeLOG:

 0.5 beta:

    GUI ADDED
  
    executable (*beta)
  
  0.8 final beta:

    bug fixes
  
    import modules moved around to prevent errors from modules not being installed
  
    fixed it allows some sites require a cookie to do a get request from them. Open the script if you need to change the default cookie
  
  
  
  
# Some ground rules
  if you haven't probably read the license before using the program as your could be using it for the wrong purpose
  
  and also before you use the program probably look at a arctic fox images or with the anime Tag because your weird
  
  this is to allow average consumers to check stock without annoying refreshing pages over and over again.
  
  
  
