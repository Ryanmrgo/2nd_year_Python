import tkinter as tk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

root = tk.Tk()
root.title("Feet to Meters")

mainframe = tk.Frame(root, padx=6, pady=6)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

feet = tk.StringVar()
meters = tk.StringVar()

feet_entry = tk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

tk.Label(mainframe, textvariable=meters).grid(column=2, row=2,
                                              sticky=(tk.W, tk.E))
tk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3,
                                                               sticky=tk.W)
tk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
tk.Label(mainframe, text="is equivalent to").grid(column=1, row=2,
                                                  sticky=tk.E)
tk.Label(mainframe, text="meters").grid(column=3, row=2,
                                        sticky=tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()
