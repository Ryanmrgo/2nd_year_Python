from tkinter import *
#from tkinter import *
#from PIL import Image
#import os
#from PIL import Image
#create root window
root=Tk()
#create canvas with color dark blue
c=Canvas(root,bg="#091e42",height=700,width=1200)
#create the house
c.create_polygon(600,250,700,200,800,250,800,400,600,400,width=2,fill="yellow",outline="red")

c.create_line(600,250,800,250,width=2,fill="red")

c.create_rectangle(650,275,750,375,fill="red")

x1,y1=0,350
x2,y2=200,450
for i in range(3):
    c.create_arc(x1,y1,x2,y2,start=0,extent=180,fill="green")
    x1+=200
    x2+=200
c.create_arc(800,350,1000,450,start=0,extent=180,fill="green")
c.create_arc(1000,350,1200,450,start=0,extent=180,fill="green")
#display moonimage
file1=PhotoImage(file="giphy.gif")
c.create_image(10,100,anchor=NW,image=file1)


#display text
id=c.create_text(600,600,text=" Home Sweet Home",font=('Helvetica',25,'bold'),fill="magenta")


c.pack()
root.mainloop()
