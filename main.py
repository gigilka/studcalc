import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Student Calculator")
app.wm_iconbitmap(r"icons/icomain.ico")

def button_event():
    print("button pressed")
    window = customtkinter.CTk()
    window.title("test")
    window.geometry("500x500")
    window.wm_iconbitmap(r"icons/icomain.ico")

    window.mainloop()


button = customtkinter.CTkButton(app, text="CTkButton", command=button_event)
button.pack()
app.mainloop()
