from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Add a Frame widget
frame = Frame(win)

# Define a function to get the data and display a message
def on_key_up():
    name = fname.get()
    frame.pack_forget()
    win.configure(bg="blue")
    Label(win, text="Hi " + name + " Welcome to home page!",
          font=('Segoe UI', 18, 'bold'), background="white").pack(pady=30)

# Create a Label widget
Label(frame, text="Registration Form",
      font=('Helvetica 16 bold'), background="blue").grid(row=0, column=0, pady=30, sticky="nsew")

# Add Field for First Name
Label(frame, text="First Name").grid(row=1, column=0, padx=5)
fname = Entry(frame)
fname.grid(row=1, column=1, padx=10)

# Add Field for Family Name
Label(frame, text="Family Name").grid(row=2, column=0, padx=5)
sname = Entry(frame)
sname.grid(row=2, column=1, padx=10)

# Add Field for Email Address
Label(frame, text="Email address").grid(row=3, column=0, padx=5)
email = Entry(frame)
email.grid(row=3, column=1, padx=10)

# Add another field for accepting password value
Label(frame, text="Enter a Password").grid(row=4, column=0, padx=5)
password = Entry(frame, show="*")
password.grid(row=4, column=1, padx=10)

# Create a button
Button(frame, text="Register", command=on_key_up).grid(row=5, columnspan=2, pady=10)

# Pack the frame
frame.pack()

win.mainloop()
