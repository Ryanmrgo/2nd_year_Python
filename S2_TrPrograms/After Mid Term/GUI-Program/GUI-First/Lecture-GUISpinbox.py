#A python program to create two spin boxes
#retrieve the values displayed in the spin boxes
#When the user click a push button
from tkinter import *
class MySpinbox:
    #constructor
    def __init__(self,root):
        #create a frame as child to root window
        self.f=Frame(root,height=350,width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #These are control variables for Spinboxes
        self.val1=IntVar()
        self.val2=StringVar()
        #create spin box with numbers from 5 to 15
        self.s1=Spinbox(self.f,from_=5,to=15,textvariable=self.val1,width=15,
                        fg='blue',bg='yellow',font=('Arial',14,'bold'))
        #create Spinbox with a tuple of strings
        self.s2=Spinbox(self.f,values=('Hyderabad','Delhi','Kolkata','Bangalore'),
                        textvariable=self.val2,width=15,fg='black',bg='LightGreen',
                        font=('Arial',14,'bold italic'))
        #create a button and bind it with display method
        self.b=Button(self.f,text='Get vaules from spin boxes',command=self.display)
        #place spin boxes and button widgets in the frame
        self.s1.place(x=50,y=50)
        self.s2.place(x=50,y=100)
        self.b.place(x=50,y=150)
    def display(self):
        #retrieve the values from the Spinbox widgets
        a=self.val1.get()
        s=self.val2.get()
        #display the values using lables
        lbl1=Label(text='Selected value is'+str(a)).place(x=50,y=220)
        lbl2=Label(text='Selected city is'+s).place(x=50,y=240)
#create the root window
root=Tk()
#create an object to MySpinbox class
mb=MySpinbox(root)
#the root window handles the mouse clik event
root.mainloop()
    






        
