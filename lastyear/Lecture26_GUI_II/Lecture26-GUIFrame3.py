#python program10 (pg.589) to create push button and bind it with an event
#handler function using command option.
from tkinter import *
class MyButton:
    #constructor
    def __init__(self,root):
        #create a frame as child to root window
        self.f=Frame(root,height=200,width=300)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #create push button as child to frame and bind it to
        #buttonClickmethod
        self.b=Button(self.f,text='My button',width=15,height=2,bg="yellow",fg="blue",activebackground="red",command=self.buttonClick())
        #attached button to frame
        self.b.pack()
    def buttonClick(self):
        print('You have clicked me')

root=Tk()
#create an object to Mybutton class
mb=MyButton(root)
#the root window handles the mouse click event
root.mainloop()

        
    

    
