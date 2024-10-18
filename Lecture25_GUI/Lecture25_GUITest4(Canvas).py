from tkinter import *
#create root window
root=Tk()
#create canvas as a child to root window
c=Canvas(root,bg='blue',height=700,width=1200,cursor='pencil')

#create a line in the canvas

id=c.create_line(50,50,200,50,200,150, width=4,fill="white")

#create an oval in the canvas
id=c.create_oval(100,100,400,300,width=5,fill="yellow",outline="red", activefill="green")


c.pack()
root.mainloop()
