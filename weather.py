from customtkinter import *
from tkinter import messagebox
import random

def get_weather():
    temperature = random.randint(-20, 40)
    descriptions = ["Sunny", "Cloudy", "Rainy", "Snowy"]
    description = random.choice(descriptions)

    messagebox.showinfo("Weather", f"Temperature: {temperature}°C\nDescription: {description}")

root = CTk()
root.title("Weather App")
root.geometry("400x300")

input_frame = CTkFrame(root)
input_frame.pack(pady=10)

button_frame = CTkFrame(root)
button_frame.pack(pady=10)

city_label = CTkLabel(input_frame, text="Enter city name:", font=("Arial", 12))
city_label.grid(row=0, column=0, padx=10)

city_entry = CTkEntry(input_frame, font=("Arial", 12))
city_entry.grid(row=0, column=1, padx=10)

get_weather_button = CTkButton(button_frame, text="Get Weather", command=get_weather, font=("Arial", 12))
get_weather_button.pack()

root.mainloop()
