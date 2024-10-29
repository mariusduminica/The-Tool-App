import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')

def destroy_function():
    global w
    w.destroy()

def button_function():
    app.destroy()  # destroy current window and creating new one
    global w
    w = customtkinter.CTk()
    w.geometry("650x490")
    w.title('Welcome')

    # Create a background label
    background_img = ImageTk.PhotoImage(Image.open("socialbkg.png"))
    background_label = customtkinter.CTkLabel(master=w, text="Welcome Back!", image=background_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add buttons and other widgets
    post_button = customtkinter.CTkButton(master=w, text="Create Post", font=('Arial', 14), corner_radius=10)
    post_button.place(x=20, y=20)

    profile_button = customtkinter.CTkButton(master=w, text="My Profile", font=('Arial', 14), corner_radius=10)
    profile_button.place(x=20, y=70)

    logout_button = customtkinter.CTkButton(master=w, text="Logout", font=('Arial', 14), corner_radius=10, command=destroy_function)
    logout_button.place(x=20, y=120)

    w.mainloop()


img1 = ImageTk.PhotoImage(Image.open("socialbkg.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3 = customtkinter.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
l3.place(x=155, y=195)

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

img2 = customtkinter.CTkImage(Image.open("google.png").resize((20, 20)))
img3 = customtkinter.CTkImage(Image.open("facebook.png").resize((20, 20)))
button2 = customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left",
                                  fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3 = customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left",
                                  fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)

# You can easily integrate authentication system

app.mainloop()