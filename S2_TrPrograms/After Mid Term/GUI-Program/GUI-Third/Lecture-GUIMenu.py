# a python program to create a menu bar and adding File and Edit Menus with some
#menu items
from tkinter import *
#from tkinter filedialog
class MyMenuDemo:
    def __init__(self,root):
        #create a menubar
        self.menubar=Menu(root)
        #attach the menu bar to the root window
        root.config(menu=self.menubar)
        #create file menu
        #Create menu items in file menu
        self.filemenu=Menu(root,tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        #self.filemenu.add_command(label="Close",command=self.donothing)
        #add horizontal line as separator
        self.filemenu.add_separator()
        #create another menu item below the separator
        self.filemenu.add_command(label="Exit",command=root.destroy)
        #add the file menu with a name 'File' to the menubar
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        #create edit menu
        self.editmenu=Menu(root,tearoff=0)
        #create menu items in edit menu
        self.editmenu.add_command(label="Cut",command=self.donothing)
        self.editmenu.add_command(label="Copy",command=self.donothing)
        self.editmenu.add_command(label="Paste",command=self.donothing)
        #add the edit menu with a name 'Edit' to the menubar
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)
    def donothing(self):
        pass
#create root window
root=Tk()
#title for the root window
root.title("A menu Example")
#create object to our class
obj=MyMenuDemo(root)
#define the size of the root window
root.geometry('600x350')
#handle any events
root.mainloop()









    
        

        

    

        
        
        

        





        
        
        
