#program 15 A pyton program to create horizontal scroll bar
from tkinter import *
class MyScrollbar:
    def __init__(self,root):
        self.t=Text(root,width=70,height=15,wrap=NONE)
        #inserrt some text into text widget
        for i in range(50):
            self.t.insert(END,"This is some text")
            self.t.pack(side=TOP,fill=X)

        #attach the text widget to the root window
        self.h=Scrollbar(root,orient=HORIZONTAL,command=self.t.xview)
        
        #attach Text widget the horizontal scroll bar
        self.t.configure(xscrollcommand=self.h.set)
        #attach scrollbar to root window at the bottom
        self.h.pack(side=BOTTOM,fill=X)


#create root window
root=Tk()
#create an object to Myscrollbar class
ms=MyScrollbar(root)
root.mainloop()
