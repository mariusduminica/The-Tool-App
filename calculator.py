import tkinter as tk

def button_click(symbol):
    current = entry.get()
    if current == "Error":
        entry.delete(0, tk.END)
    if symbol == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 16), bd=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=column)

root.mainloop()
