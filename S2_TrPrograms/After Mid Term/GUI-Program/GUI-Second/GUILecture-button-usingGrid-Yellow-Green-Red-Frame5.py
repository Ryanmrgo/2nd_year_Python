#Arrange widgets in Frame
#
from tkinter import *
class MyButton:
    #constructor
    def __init__(self,root):
        #create a frame as child to root window
        self.frame=Frame(root,height=700,width=900)
        #let the frame will not shrink
        self.frame.propagate(0)
        #attach the frame to root window
        self.frame.pack()
        #create push button as child to frame and bind it to
        #buttonClickmethod3 pushed button
        self.b1=Button(self.frame,text='Yellow',width=15,height=2,
                       command=lambda:self.buttonClick(1))
        self.b2=Button(self.frame,text='Green',width=15,height=2,
                       command=lambda:self.buttonClick(2))
        self.b3=Button(self.frame,text='Red',width=15,height=2,
                       command=lambda:self.buttonClick(3))
        #attached button to frame
        '''
        self.b1.pack(side=LEFT,padx=10,pady=15)#occupies vertically, Space on X axis.
       # self.b1.pack(fill=Y)
        self.b2.pack(side=RIGHT,padx=10,pady=15)
        #self.b2.pack(fill=Y)
        self.b3.pack(fill=X)
        #self.b3.pack(fill=Y)
        '''
        self.b1.grid(row=0,column=0,padx=10,pady=15) #display in 0 th row,
        self.b2.grid(row=0,column=1,padx=10,pady=15) #display in with spaces
        self.b3.grid(row=0,column=2,padx=10,pady=15) #display in with spaces
        
    def buttonClick(self,num):
        if num==1:
            self.frame["bg"]='yellow'
        if num==2:
            self.frame["bg"]='green'
        if num==3:
            self.frame["bg"]='red'
        
            
       
        print('You have clicked me')
root=Tk()
#create an object to Mybutton class
mb=MyButton(root)
#the root window handles the mouse click event
root.mainloop()
        
    

    
