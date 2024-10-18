from tkinter import *

# Function to be called when the button is clicked
def buttonClick():
    print('You have clicked me')

# Create root window
root = Tk()

# Create a frame inside the root window
frame = Frame(root,height=200,width=300)
#let the frame will not shrink
frame.propagate(0)
# Attach the frame to the root window
frame.pack()

# Create a button inside the frame
button = Button(frame, text='Click Me', command=buttonClick)

# Attach the button to the frame
button.pack()

# Run the application
root.mainloop()
