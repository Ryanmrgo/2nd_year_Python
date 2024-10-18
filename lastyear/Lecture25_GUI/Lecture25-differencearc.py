from tkinter import *
#create root window
root=Tk()
#create canvas
c=Canvas(root,bg='white',height=700,width=1200)
#create arcs in the canvas
id=c.create_arc(100,100,400,300,width=3,start=270,extent=180,outline='red',style='arc')
id=c.create_arc(500,100,800,300,width=3,start=90,extent=180,outline='green',style='arc')
id=c.create_arc(100,400,400,600,width=3,start=0,extent=180,outline='blue',style='arc')


#add canvas to the root
c.pack()
#wait for any events
root.mainloop()
