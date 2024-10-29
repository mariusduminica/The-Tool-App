# Import libraries
from customtkinter import*
from PIL import Image, ImageTk

# Open the app
def open_clock():
    os.system('clock.py')

def open_weather():
    os.system('weather.py')

def open_calculator():
    os.system('calculator.py')

def open_snakegame():
    os.system('snakegame.py')

def open_music():
    os.system('music.py')

def open_wallet():
    os.system('wallet.py')

def open_contacts():
    os.system('contacts.py')

def open_paint():
    os.system('paint.py')

def open_notes():
    os.system('notes.py')

# Window details
root = CTk()
root.geometry("640x490")
root.title("Tool App")
set_appearance_mode("dark")
set_default_color_theme("dark-blue")

# Load and set the background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((640, 490))  # Match to window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Add a label with the background image
bg_label = CTkLabel(root, image=bg_photo, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Welcome text
CTkLabel(root, text="Welcome to The Tool App", font=("Arial", 25),
         fg_color="purple", anchor="center"
         ).grid(column=1, row=0, pady=10, padx=10)

# Frame of button
clock = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=0, row=1, pady=10, padx=10)

weather = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=0, row=2, pady=10, padx=10)

calculator = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=0, row=3, pady=10, padx=10)

snakegame = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=1, row=3, pady=10, padx=10)

music = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=1, row=1, pady=10, padx=10)

wallet = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=1, row=2, pady=10, padx=10)

contacts = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=2, row=1, pady=10, padx=10)

paint = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=2, row=2, pady=10, padx=10)

notes = CTkFrame(root, bg_color="purple", fg_color="purple",
                 border_color="black", height=100, width=100
                 ).grid(column=2, row=3, pady=10, padx=10)

# Load image for clock button
clock_image = Image.open("clockbtn.png")
width, height = 64, 64
clock_image = clock_image.resize((width, height))
clock_photo = ImageTk.PhotoImage(clock_image)

# Load image for weather button
weather_image = Image.open("weatherbtn.png")
width, height = 64, 64
weather_image = weather_image.resize((width, height))
weather_photo = ImageTk.PhotoImage(weather_image)

# Load image for calculator button
calculator_image = Image.open("calculatorbtn.png")
width, height = 64, 64
calculator_image = calculator_image.resize((width, height))
calculator_photo = ImageTk.PhotoImage(calculator_image)

# Load image for snakegame button
snakegame_image = Image.open("snakegamebtn.png")
width, height = 64, 64
snakegame_image = snakegame_image.resize((width, height))
snakegame_photo = ImageTk.PhotoImage(snakegame_image)

# Load image for music button
music_image = Image.open("musicbtn.png")
width, height = 64, 64
music_image = music_image.resize((width, height))
music_photo = ImageTk.PhotoImage(music_image)

# Load image for wallet button
wallet_image = Image.open("walletbtn.png")
width, height = 64, 64
wallet_image = wallet_image.resize((width, height))
wallet_photo = ImageTk.PhotoImage(wallet_image)

# Load image for contacts button
contacts_image = Image.open("contactsbtn.png")
width, height = 64, 64
contacts_image = contacts_image.resize((width, height))
contacts_photo = ImageTk.PhotoImage(contacts_image)

# Load image for paint button
paint_image = Image.open("paintbtn.png")
width, height = 64, 64
paint_image = paint_image.resize((width, height))
paint_photo = ImageTk.PhotoImage(paint_image)

# Load image for notes button
notes_image = Image.open("notesbtn.png")
width, height = 64, 64
notes_image = notes_image.resize((width, height))
notes_photo = ImageTk.PhotoImage(notes_image)

# Load buttons
CTkButton(clock, image=clock_photo, text="Clock", command=open_clock, height=64, width=64).grid(row=1, column=0, pady=10, padx=10)
CTkButton(weather, image=weather_photo, text="Weather", command=open_weather, height=64, width=64).grid(row=2, column=0, pady=10, padx=10)
CTkButton(calculator, image=calculator_photo,text="Calculator", command=open_calculator, height=64, width=64).grid(row=3, column=0, pady=10, padx=10)
CTkButton(snakegame, image=snakegame_photo, text="SnakeGame", command=open_snakegame, height=64, width=64).grid(row=3, column=1, pady=10, padx=10)
CTkButton(music, image=music_photo, text="Music", command=open_music, height=64, width=64).grid(row=1, column=1, pady=10, padx=10)
CTkButton(wallet, image=wallet_photo, text="Wallet", command=open_wallet, height=64, width=64).grid(row=2, column=1, padx=10, pady=10)
CTkButton(contacts, image=contacts_photo, text="Contacts", command=open_contacts, height=64, width=64).grid(row=1, column=2, padx=10, pady=10)
CTkButton(paint, image=paint_photo, text="Paint", command=open_paint, height=64, width=64).grid(row=2, column=2, padx=10, pady=10)
CTkButton(notes, image=notes_photo, text="Notes", command=open_notes, height=64, width=64).grid(row=3, column=2, padx=10, pady=10)

# Maintain the app so it doesnt close
root.mainloop()