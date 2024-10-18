# a python program to create 3 check buttons and konw which options are selected by user
from tkinter import *
class Mycheck:
    #constructor
    def __init__(self,root):
        #create a frame
        self.f=Frame(root,height=350,width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to the window
        self.f.pack()
        #create IntVar class vairables
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        #create check boxs and bind them to display method
        self.c1=Checkbutton(self.f,bg='gray',fg='green',variable=self.var1,command=self.display)
        self.c2=Checkbutton(self.f,bg='gray',fg='green',variable=self.var2,command=self.display)
        self.c3=Checkbutton(self.f,bg='gray',fg='green',variable=self.var3,command=self.display)
        #attach check boxes to the frame
        self.c1.place(x=50,y=100)
        self.c2.place(x=200,y=100)
        self.c3.place(x=350,y=100)
    def display(self):
        #restrict the control variables values
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()
        #string is empty
        str1=''
        str2=''
        str3=''
        #catch user choice
        if x==1:
            str1=' java'
        if y==1:
            str2=' python'
        if z==1:
            str3=' .Net'
        #display the user selection as label
            
        lbl=Label(text=str1,fg='blue').place(x=50,y=150,width=100,height=20)
        lbl=Label(text=str2,fg='blue').place(x=50,y=200,width=100,height=20)
        lbl=Label(text=str3,fg='blue').place(x=50,y=250,width=100,height=20)
        
root=Tk()
mb=Mycheck(root)
root.mainloop







            

        
            
        





        




        
