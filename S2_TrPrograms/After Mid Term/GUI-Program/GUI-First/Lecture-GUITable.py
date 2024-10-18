#A GUI Program to display  a table with several rows and columns
from tkinter import *
class MyTable:
    def __init__(self,root):
        #code for creating the table
        for i in range (total_rows):
            for j in range (total_cols):
                self.e=Entry(root,width=20,fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i,column=j)
                self.e.insert(END,lst[i][j])
lst=[(1001,'Geeta Kumari','Chandigarh',1207.88),(1002,'Ko Ko','Mandanlay',127.88)]
#find the no.of rows and cols in the list
total_rows=len(lst)
total_cols=len(lst[0])
#create root window
root=Tk()
mt=MyTable(root)
root.mainloop()
