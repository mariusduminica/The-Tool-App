import tkinter as tk
from PIL import ImageTk, Image
import random

def add_1000():
    global total
    total += 1045.77
    update_label()
    # Disable Button 1 for 15 seconds
    button1.config(state="disabled")
    root.after(15000, enable_button1)

def subtract_500():
    global total
    total -= 504.94
    update_label()
    root.after(35000, calculate_sum)

def calculate_sum():
    global total
    numbers = [1027.67, 10.99, 129.78, 739.34, 350.55]
    total += sum(numbers)
    update_label()

def add_random():
    global total
    # Add random amount not exceeding 0.99
    total -= 0.01
    update_label()
    total += random.uniform(0, 0.99)
    update_label()

def enable_button1():
    button1.config(state="normal")

def enable_button2():
    button2.config(state="normal")

def update_label():
    label.config(text=f"${total:.2f}")

total = 0.00

root = tk.Tk()
root.title("Wallet")
root.geometry("200x200")

image = Image.open("wallet.png")
image = image.resize((50, 50)) # Resize the image if needed
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

label = tk.Label(root, text=f"${total:.2f}", font=("Arial", 18))
label.pack()

button1 = tk.Button(root, text="Work (+1045.77)", command=add_1000)
button1.pack()

button2 = tk.Button(root, text="Invest (-500.94)", command=subtract_500)
button2.pack()

button3 = tk.Button(root, text="Mine (-0.01)", command=add_random)
button3.pack()

root.mainloop()


