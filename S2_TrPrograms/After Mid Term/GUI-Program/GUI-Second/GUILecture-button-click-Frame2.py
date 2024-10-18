'''What are the layout managers in Python?
The Python tkinter library includes three layout managers, place , pack , and grid . The place layout manager can be used to place elements on the screen at specific x-y coordinates.
'''
'''
import tkinter as tk
def button_click_handler(event):
    label.config(text="Button Clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me")
button.pack()
label = tk.Label(root, text="")
label.pack()
button.bind("<Button-1>", button_click_handler)
root.mainloop()

'''

import tkinter as tk

root = tk.Tk()

# Function to retrieve the entry data
def get_entry_data():
    data = entry.get()
    print("Entry data:", data)

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create an entry widget with show='*'
entry = tk.Entry(frame, show='*')
entry.pack(side=tk.LEFT)

# Create a button to retrieve the entry data
button = tk.Button(frame, text="Get Data", command=get_entry_data)
button.pack(side=tk.LEFT, padx=5)

root.mainloop()


