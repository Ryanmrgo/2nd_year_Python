#A GUI program to display a menu and aslo to open a file and save it throug the file dialog box
from tkinter import *
from tkinter import filedialog

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
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
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
    #method for opening a file and a display its contents in the text box
    def open_file(self):
        #open a file dialog box and accept the file name
        self.filename=filedialog.askopenfilename(parent=root,title='select a file',filetypes=(("python files","*.py"),("Allfiles","*.*")))
        #if cancel button is not clicked in the dialog box
        if self.filename!=None:
            #open the file in read mode
            f=open(self.filename,'r')
            #read the contents of the file
            contents=f.read()
            #Create a text box and add it the root window
            self.t=Text(root,width=80,height=20,wrap=WORD)
            self.t.pack()
            #insert the file contents to the Text box
            self.t.insert(1.0,contents)
            #close the file
            f.close()

    def save_file(self):
        # open file dialog box and type a file name
        self.filename=filedialog.asksaveasfilename(parent=root,defaultextension=".txt")
        #if cancel button is not clicked in the text box
        if self.filename!=None:
            #open the file in read mode
            f=open(self.filename,'w')
            #get the contents of the text box
            contents=str(self.t.get(1.0,END))
            #store the file contents into the File
            f.write(contents)
            #close the file
            f.close()
            
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
