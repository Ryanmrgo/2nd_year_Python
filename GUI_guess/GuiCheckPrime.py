import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime():
    try:
        number = int(entry.get())  # Get the number entered by the user
        if is_prime(number):
            messagebox.showinfo("Result", f"{number} is prime")
        else:
            messagebox.showinfo("Result", f"{number} is not prime")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Create the main window
root = tk.Tk()
root.title("Prime Checker")

# Create and pack widgets
label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_prime)
check_button.pack()

# Run the main event loop
root.mainloop()
