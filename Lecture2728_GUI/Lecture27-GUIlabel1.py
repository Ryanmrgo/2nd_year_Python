from tkinter import *

class MyButtons:
    #constructor
    def __init__(self,root):
        # create a frame as child to root window
        self.f=Frame(root,height=100,width=150)
        #let the frame will not shrik
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #Create a push button and bind it to the button click method
        self.b1=Button(self.f,text="Click Me",width=15,height=2,command=self.buttonClick)
        #Create another button that closes the root window upon clicking
        self.b2=Button(self.f,text='Close',width=15,height=2,command=self.close_window)
        #attach button to a frame
        self.b1.grid(row=0,column=1)
        self.b2.grid(row=0,column=5)

        #the event handler method
    def buttonClick(self):
        #create a label with some text
        self.lbl= Label(self.f,text=" Welcome to Python",width=20,height=2,font=('Courer',-30,'bold'),fg='blue')
        #attach the label in the frame
        self.lbl.grid(row=2,column=1)
    def close_window(self):
        root.destroy()

#Create root window
root=Tk()
#Create an object to Mybutton Class
mb=MyButtons(root)
#the root window handles the mouse click event
root.mainloop()






        
