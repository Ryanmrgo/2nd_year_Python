#https://www.tutorialspoint.com/creating-a-tkinter-gui-layout-using-frames-and-grid
# Import the Required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Add a Frame widget
frame = Frame(win)

# Define a function to get the data and display a message
def on_key_up():
   name = fname
   frame.pack_forget()
   win.configure(bg="green4")
   Label(win, text="Hey " + fname.get() + " Welcome to first Frame Test for registration",
      font=('Segoe UI', 18, 'bold'),
      background="white").pack(pady=30)
# Create a Label widget
   Label(frame, text="Registration Form",
   font=('Helvetica 16 bold'),
background="green3").grid(row=5, column=0, pady=30)
frame.pack()

# Add Field for First Value
Label(frame, text="First Name").grid(row=7, column=0, padx=5)
fname = Entry(frame)
fname.grid(row=10, column=0, padx=10)

# Add Field for Second Value
Label(frame, text="Family name").grid(row=12, column=0, padx=5)
sname = Entry(frame)
sname.grid(row=15, column=0, padx=10)

# Add Field for Email Address
Label(frame, text="Email address").grid(row=17, column=0, padx=5)
email = Entry(frame)
email.grid(row=20, column=0, padx=10)

# Add another field for accepting password value
Label(frame, text="Enter a Password").grid(row=22, column=0, padx=5)
password = Entry(frame, show="*")
password.grid(row=25, column=0, padx=10)

# Create a button
Button(frame, text="Register", command=on_key_up).grid(row=15,
column=1, padx=5)

win.mainloop()
