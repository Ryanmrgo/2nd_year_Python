#  A python program to display a message in the frame
from tkinter import *
class MyMessage:
    #constructor
    def __init__(self,root):
        #create a frame as a child to the root window
        self.f=Frame(root,height=300,width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to the root window
        self.f.pack()
        #create a message widget with some text
        
        self.m=Message(self.f,text="This is the message before you delete the data please check",width=200,font=('Roman',20,'bold italic'),fg='dark goldenrod')
        #attach message to the frame
        self.m.pack(side=LEFT)
        
#create root window
root=Tk()
#create an object to Mymessage class
mb=MyMessage(root)
#the root window handles the mouse Click event
root.mainloop()
