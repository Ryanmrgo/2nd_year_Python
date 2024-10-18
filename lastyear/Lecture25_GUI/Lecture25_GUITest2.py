#A python program to create root window with some options
from tkinter import *
#create top level window
root=Tk()
#set window title
root.title("Test for Title")
#set window size
root.geometry("400x300")
#set window icon
#root.wm_iconbitmap('Test.ico')
root.iconbitmap(r'C:\Users\MIIT-ITSM02\Desktop\Lecture25\Lecture25-GUIPrograms1\Test.ico') 

#display window and wait for any events
root.mainloop()
