import tkinter as tk
from tkinter import messagebox

def Check_armstrong():
    num = int(entry.get())
    sum = 0
    temp = num
    
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if num == sum:
       result_label.config(text=f"{num} is a Armstrong number")
      # messagebox.showinfo("Result", f"{num} is a Armstrong number")
    else:
      #messagebox.showinfo("Result", f"{num} is not an Armstrong number")
        
        result_label.config(text=f"{num} is not an Armstrong number")
def reset():
    entry.delete(0, 5)
    result_label.destroy

    
# Create the main window
root = tk.Tk()

root.title("Armstrong_checker")
root.geometry("350x250")
# Create and pack widgets
label = tk.Label(root, text="Armstrong Number Checker", font=("Verdana", 16,'bold')).place(x = 10,y = 10)

entry_label = tk.Label(root, text='Enter a number:').place(x = 30,y = 50)  

entry = tk.Entry(root,text="Enter a number:").place(x = 140,y = 50)


calculate_button = tk.Button(root, text="Check", command=Check_armstrong).place(x = 300,y = 50) 

reset_button = tk.Button(root, text="Reset", command=reset).place(x = 300,y = 90)



#Button(root, text="Reset", width=10, height=1, command=reset).pack()

result_label = tk.Label(root, text="",font=("Arial",12))

# Run the main event loop

root.mainloop()
