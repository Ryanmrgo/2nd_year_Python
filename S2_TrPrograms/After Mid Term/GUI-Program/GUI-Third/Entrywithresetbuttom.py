import tkinter as tk

def reset():
    username_entry.delete(0, tk.END)  # Clear the username entry widget
    password_entry.delete(0, tk.END)  # Clear the password entry widget

def submit():
    username = username_entry.get()
    password = password_entry.get()
    
    print(f"Username: {username}")
    print(f"Password: {password}")

app = tk.Tk()
app.title("Login Page")

# Username label and entry widget
username_label = tk.Label(app, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(app)
username_entry.pack(pady=10)

# Password label and entry widget
password_label = tk.Label(app, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(app, show="*")  # Show * for password
password_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(app, text="Submit", command=submit)
submit_button.pack(pady=10)

# Reset button
reset_button = tk.Button(app, text="Reset", command=reset)
reset_button.pack(pady=10)

app.mainloop()
