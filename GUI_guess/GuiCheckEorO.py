import tkinter as tk
from tkinter import messagebox

def check_even_odd():
    try:
        number = int(entry.get())  # Get the number entered by the user
        if number % 2 == 0:
            messagebox.showinfo("Result", f"{number} is even")
        else:
            messagebox.showinfo("Result", f"{number} is odd")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Create the main window
root = tk.Tk()
root.title("Even/Odd Checker")

# Create and pack widgets
label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_even_odd)
check_button.pack()

# Run the main event loop
root.mainloop()
