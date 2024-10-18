#python program10 (pg.589) to create push button and bind it with an event
#handler function using command option.
from tkinter import *
class MyButton:
    #constructor
    def __init__(self,root):
        #create a frame as child to root window
        self.f=Frame(root,height=400,width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #create push button as child to frame and bind it to
        #buttonClickmethod3 pushed button
        self.b1=Button(self.f,text='Yellow',width=15,height=2,
                       command=lambda:self.buttonClick(1))
        self.b2=Button(self.f,text='Green',width=15,height=2,
                       command=lambda:self.buttonClick(2))
        self.b3=Button(self.f,text='Red',width=15,height=2,
                       command=lambda:self.buttonClick(3))

        #attached button to frame
        #self.b1.pack()
        self.b1.pack(side=LEFT,padx=10,pady=15)
        #self.b2.pack()
        self.b2.pack(side=RIGHT,padx=10,pady=15)
        #self.b3.pack()
        self.b3.pack(fill=X)  #default center
'''
#you can use place
        self.b2.place(x=200,y=100,width=100,height=300)# display(200,100)
        self.b1.place(x=20,y=30,width=100,height=50)   # display(20,30)
        self.b3.place(x=20,y=100,width=100,height=150) # display(20,30)
'''
                
def buttonClick(self,num):
        if num==1:
            self.f["bg"]='yellow'
        if num==2:
            self.f["bg"]='green'
        if num==3:
            self.f["bg"]='red'   
       
        print('You have clicked me')
root=Tk()
#create an object to Mybutton class
mb=MyButton(root)
#the root window handles the mouse click event
root.mainloop()
        
    

    
