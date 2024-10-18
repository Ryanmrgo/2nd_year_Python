import tkinter as tk
from tkinter import messagebox

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial():
    try:
        number = int(entry.get())  # Get the number entered by the user
        if number < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer")
        else:
            result = factorial(number)
            messagebox.showinfo("Result", f"The factorial of {number} is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Create the main window
root = tk.Tk()
root.title("Factorial Calculator")

# Create and pack widgets
label = tk.Label(root, text="Enter a non-negative integer:")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_factorial)
calculate_button.pack()

# Run the main event loop
root.mainloop()
