import datetime
from tkinter import *

root=Tk()

def start():
    global start
    start=datetime.datetime.now()
    print(start)
    
def laptime():
    global lap
    lap=datetime.datetime.now()
    print(lap)
    lap=lap-start
    print(lap)
    
def stop():
    global stop
    stop=datetime.datetime.now()
    print (stop)
    delta=stop-start
    print(delta)

startb = Button(root, text="Start", command=start)
startb.pack()
lapb = Button(root, text="Lap", command=laptime)
lapb.pack()
stopb = Button(root, text="Stop", command=stop)
stopb.pack()

mainloop()
