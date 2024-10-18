# A python program to create a Text widget with a vertical
#scroll bar attached to it. also highlight the first line of the text and display an image in the text widget
from tkinter import *

class MyText:
    #constructor
    def __init__(self,root):
        #create a Text widget with 20 chars width and 10 lines height
        self.t=Text(root,width=20,height=10,font=('Verdana',14,'bold'),fg='blue',bg='yellow',wrap=NONE)
        
        #insert some text into the Text widgets
        self.t.insert(END,"Text Widget Test\n   this is the first line ")
        #attach Text to the root
        self.t.pack(side=LEFT)
        #Show image in the Text widget
        
        self.img=PhotoImage(file='tt1.gif')
        self.t.image_create(END,image=self.img)
        
        #create a tag with the name start
        self.t.tag_add('start','1.0','1.11')
        #apply color to the tag
        self.t.tag_config('start',background='red',foreground='white',font=('Lucida console',20,'bold italic'))
        

        #create a scroll bare widget
        '''
        self.s=Scrollbar(root,orient=VERTICAL,command=self.t.yview)
        #attach the scroll bar to the Text widget
        self.t.configure(yscrollcommand=self.s.set)
        #attach the scroll bar to the root windwo
        self.s.pack(side=RIGHT,fill=Y)
        '''
#create a root window
root=Tk()
#create an object to MyText class

mt=MyText(root)

#the root window handles the mouse click event
root.mainloop()





        


        
        



        
        
