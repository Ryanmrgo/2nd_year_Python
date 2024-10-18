from tkinter import *

def convert_currency():
    amount = float(entry.get())
    if var.get() == 1:
        result_label.config(text=f"INR: {amount * 74.5}")
    elif var.get() == 2:
        result_label.config(text=f"USD: {amount / 74.5}")

app = Tk()
app.title("Currency Converter")

Label(app, text="Enter Amount:").pack(pady=10)
entry = Entry(app)
entry.pack(pady=10)

var = IntVar()
Radiobutton(app, text="USD to INR", variable=var, value=1).pack()
Radiobutton(app, text="INR to USD", variable=var, value=2).pack()

Button(app, text="Convert", command=convert_currency).pack(pady=10)

result_label = Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
