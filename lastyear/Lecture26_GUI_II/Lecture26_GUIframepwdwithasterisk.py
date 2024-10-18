from tkinter import *

def submit():
    username = e1.get()
    password = e2.get()
    print("Username:", username)
    print("Password:", password)  # You can replace this with your desired action

top = Tk()

top.geometry("400x250")

# Creating label
uname = Label(top, text="Username")
uname.place(x=30, y=50)

# Creating label
password = Label(top, text="Password")
password.place(x=30, y=90)

sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue", command=submit)
sbmitbtn.place(x=30, y=120)

e1 = Entry(top, width=20)
e1.place(x=100, y=50)

e2 = Entry(top, width=20, show="*")  # Set show attribute to "*"
e2.place(x=100, y=90)

top.mainloop()
