from tkinter import *
#create root window
root=Tk()
#give a title for root window
root.title("My Frame")
#create as child to root window
f=Frame(root,height=400,width=500,bg="yellow",cursor="cross")
#attach the frame to root window
f.pack()
#let the rootwindow wait for any events
root.mainloop()
