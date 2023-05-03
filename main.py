import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Student Calculator")


def button_event():
    print("button pressed")
    window = customtkinter.CTk()
    window.geometry("500x500")
    window.mainloop()


button = customtkinter.CTkButton(app, text="CTkButton", command=button_event)
button.pack()
app.mainloop()
