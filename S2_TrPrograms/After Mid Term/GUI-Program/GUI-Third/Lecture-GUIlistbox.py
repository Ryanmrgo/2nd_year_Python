#Python program to create list box
#with the universities names and display the selected universities names in a text bos
from tkinter import *
class ListboxDemo:
    def __init__(self,root):
        self.f=Frame(root,width=700,height=400)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #create a label
        self.lbl=Label(self.f,text='Click one or more of the Universities below:',font="Calibri 14")
        self.lbl.place(x=50,y=50)
        #Create the list boxes with the universities names
        self.lb=Listbox(self.f,font="Arial 12 bold",fg='blue',bg='yellow',height=8,selectmode=MULTIPLE)
        self.lb.place(x=50,y=100)
        #using for loop insert items into the list boxes
        for i in ["Stanford University","Oxford University","Texas A&M University","Cambridge Uinversity","University of Califonia"]:
            self.lb.insert(END,i)
            #bind the listboxSelect event to on_select() method
            self.lb.bind('<<ListboxSelect>>',self.on_select)
        #Create text box to display the selected items
        self.t=Text(self.f,width=40,height=6,wrap=WORD)
        self.t.place(x=300,y=100)
    def on_select(self,event):
        #create an empty list box
        self.lst=[]
        #know the indexes of the selected items
        indexes=self.lb.curselection()
        #retrieve the item name depending on the indexes
        #append the items names to the list box
        for i in indexes:
            self.lst.append(self.lb.get(i))
        #delete the previous content of the text box
        self.t.delete(0.0,END)
        #insert the new contents into the text box
        self.t.insert(0.0,self.lst)
#create the root window
root=Tk()
#title the root window
root.title("List box demonstrations")
#create obj to our class
obj=ListboxDemo(root)
#handle any events
root.mainloop()






        










        
    
